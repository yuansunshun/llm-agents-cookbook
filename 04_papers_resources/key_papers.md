# 精读论文笔记

## Transformer 基础

### Attention Is All You Need (2017)
- **作者**：Vaswani et al.，Google Brain
- **核心贡献**：提出纯注意力机制的 Seq2Seq 架构，取代 RNN/CNN
- **关键公式**：$\text{Attention}(Q,K,V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$
- **要点**：多头注意力允许模型同时关注不同位置的不同表示子空间

---

## RAG

### Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (2020)
- **作者**：Lewis et al.，Facebook AI
- **核心贡献**：将检索模块与生成模型结合，解决 LLM 知识截止和幻觉问题

---

## Agents

### ReAct: Synergizing Reasoning and Acting in Language Models (2022)
- **作者**：Yao et al.
- **核心贡献**：让 LLM 交替生成推理轨迹（Thought）和动作（Action），显著提升工具使用能力

---

> 持续更新中...
