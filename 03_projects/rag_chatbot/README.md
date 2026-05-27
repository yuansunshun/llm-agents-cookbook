# RAG 问答机器人

基于检索增强生成（RAG）的本地知识库问答系统。

## 功能

- 上传本地文档（PDF / TXT / Markdown）
- 自动切分、向量化并存入 ChromaDB
- 用户提问时检索相关片段，结合 LLM 生成有依据的回答

## 快速开始

```bash
# 安装依赖
pip install -r ../../requirements.txt

# 配置 API Key
cp ../../.env.example .env
# 编辑 .env 填入 OPENAI_API_KEY

# 运行
python main.py
```

## 结构

```
rag_chatbot/
├── main.py        # 入口：加载文档、构建索引、问答循环
├── demo.ipynb     # 交互式演示，逐步展示每个环节
└── README.md
```
