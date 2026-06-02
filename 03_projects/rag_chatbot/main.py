"""
RAG Chatbot — CLI 版本
用法：python main.py --file path/to/document.pdf
"""
import os
import sys
import argparse
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

# ── 依赖检测 ──────────────────────────────────────────────────
try:
    import anthropic
    import chromadb
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("请先安装依赖：pip install anthropic chromadb sentence-transformers PyMuPDF python-dotenv")
    sys.exit(1)


# ── 文本提取 ──────────────────────────────────────────────────
def extract_text(file_path: str) -> str:
    path = Path(file_path)
    if path.suffix.lower() == ".pdf":
        import fitz  # PyMuPDF
        doc = fitz.open(file_path)
        return "\n".join(page.get_text() for page in doc)
    elif path.suffix.lower() in (".txt", ".md"):
        return path.read_text(encoding="utf-8")
    else:
        raise ValueError(f"不支持的文件格式：{path.suffix}")


# ── 切块 ──────────────────────────────────────────────────────
def chunk_text(text: str, chunk_size: int = 400, overlap: int = 80) -> list[str]:
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunks.append(" ".join(words[start:end]))
        if end == len(words):
            break
        start += chunk_size - overlap
    return [c for c in chunks if len(c.strip()) > 30]


# ── 向量数据库 ─────────────────────────────────────────────────
class VectorStore:
    def __init__(self, collection_name: str = "rag_docs"):
        self.client = chromadb.Client()
        self.embed_model = SentenceTransformer("all-MiniLM-L6-v2")
        # 每次运行重建集合
        try:
            self.client.delete_collection(collection_name)
        except Exception:
            pass
        self.collection = self.client.create_collection(collection_name)

    def add_documents(self, chunks: list[str], source: str) -> None:
        if not chunks:
            return
        embeddings = self.embed_model.encode(chunks).tolist()
        self.collection.add(
            documents=chunks,
            embeddings=embeddings,
            ids=[f"{source}_{i}" for i in range(len(chunks))],
            metadatas=[{"source": source, "chunk_id": i} for i in range(len(chunks))],
        )
        print(f"  已索引 {len(chunks)} 个文本块")

    def search(self, query: str, top_k: int = 3) -> list[dict]:
        query_embedding = self.embed_model.encode([query]).tolist()
        results = self.collection.query(
            query_embeddings=query_embedding,
            n_results=min(top_k, self.collection.count()),
        )
        docs, metas, dists = results["documents"][0], results["metadatas"][0], results["distances"][0]
        return [
            {"text": doc, "source": meta["source"], "chunk_id": meta["chunk_id"], "score": 1 - dist}
            for doc, meta, dist in zip(docs, metas, dists)
        ]


# ── RAG 生成 ──────────────────────────────────────────────────
def generate_answer(
    query: str,
    retrieved: list[dict],
    history: list[dict],
    client: anthropic.Anthropic,
    model: str = "claude-sonnet-4-6",
) -> str:
    context = "\n\n".join(
        f"[来源 {i+1}] {r['text']}" for i, r in enumerate(retrieved)
    )

    system = (
        "你是一个基于文档回答问题的助手。\n"
        "只使用提供的上下文片段回答。\n"
        "如果文档中没有相关信息，明确说明「文档中未找到相关信息」。\n"
        "回答末尾以「📎 来源：[来源 X]」格式标注引用。"
    )

    messages = history + [
        {
            "role": "user",
            "content": f"上下文：\n{context}\n\n问题：{query}",
        }
    ]

    response = client.messages.create(
        model=model,
        max_tokens=1024,
        system=system,
        messages=messages,
    )
    return response.content[0].text


# ── 主程序 ────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="RAG Chatbot")
    parser.add_argument("--file", required=True, help="文档路径（PDF 或 TXT）")
    parser.add_argument("--top-k", type=int, default=3, help="检索 chunk 数量")
    args = parser.parse_args()

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("错误：请设置 ANTHROPIC_API_KEY 环境变量")
        sys.exit(1)

    print(f"\n正在加载文档：{args.file}")
    text = extract_text(args.file)
    chunks = chunk_text(text)
    print(f"切块完成：{len(chunks)} 个 chunk")

    print("正在建立向量索引...")
    store = VectorStore()
    store.add_documents(chunks, source=Path(args.file).name)

    client = anthropic.Anthropic(api_key=api_key)
    history: list[dict] = []

    print("\n✅ 准备就绪！输入问题开始对话（输入 'quit' 退出，'clear' 清空历史）\n")

    while True:
        try:
            query = input("你: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n再见！")
            break

        if not query:
            continue
        if query.lower() == "quit":
            print("再见！")
            break
        if query.lower() == "clear":
            history.clear()
            print("对话历史已清空\n")
            continue

        retrieved = store.search(query, top_k=args.top_k)
        answer = generate_answer(query, retrieved, history, client)

        print(f"\nAI: {answer}\n")

        # 维护对话历史（只保留最近 6 轮以控制 token）
        history.append({"role": "user", "content": query})
        history.append({"role": "assistant", "content": answer})
        if len(history) > 12:
            history = history[-12:]


if __name__ == "__main__":
    main()
