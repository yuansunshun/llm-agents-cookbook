# 模块一：LLM 基础原理

## 学习目标

理解大语言模型的核心机制，为后续使用各类框架打下理论基础。

## 笔记列表

| 文件 | 主题 | 说明 |
|------|------|------|
| [01_transformer_arch.ipynb](01_transformer_arch.ipynb) | Transformer 架构 | 编码器/解码器结构、自注意力计算过程 |
| [02_tokenization.ipynb](02_tokenization.ipynb) | 分词与词嵌入 | BPE、词表、token 计数与成本估算 |
| [03_prompting.ipynb](03_prompting.ipynb) | Prompt Engineering | Zero-shot、Few-shot、CoT、System Prompt 设计 |
| [04_rag_intro.ipynb](04_rag_intro.ipynb) | RAG 入门 | 检索增强生成原理、向量数据库基础 |

## 关键概念速查

- **Token**：模型处理文本的最小单元，约 0.75 个英文单词
- **Context Window**：模型一次能处理的最大 token 数
- **Temperature**：控制输出随机性，0 = 确定性，1+ = 更有创意
- **Embedding**：将文本映射为高维向量，语义相似的文本向量相近
