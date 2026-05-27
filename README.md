# LLM & Agents Cookbook 🍳

> **中文** | 大语言模型与 AI Agents 系统学习笔记，以 Jupyter Notebook 为主要载体。
> 覆盖原理推导、框架实践和完整项目，面向有一定编程基础的学习者。

---

## 这个仓库是什么？

本仓库是一套**由浅入深**的 LLM 学习教程，每个知识点都力求做到：

- **讲清楚「为什么」**：不止告诉你怎么用，更解释背后的设计动机
- **数学推导 + 代码验证**：公式不是摆设，配套可运行的 NumPy 实现
- **大量可视化**：注意力权重、位置编码、BPE 合并过程、温度采样效果……用图说话
- **生产级视角**：每个环节都指出实践中的坑、性能权衡和推荐配置

---

## 学习路线图

```
01_llm_basics/          ← 从这里开始
    01_transformer_arch         Transformer 架构全面解析
    02_tokenization             分词与词嵌入
    03_prompting                Prompt Engineering 完全指南
    04_rag_intro                RAG 检索增强生成

02_agents_frameworks/   ← 进阶：主流框架实践（规划中）
    01_langchain_basics         LangChain 链式调用
    02_llama_index_rag          LlamaIndex 知识库
    03_autogen_multiagent       AutoGen 多智能体
    04_claude_agent_sdk         Claude Agent SDK

03_projects/            ← 完整项目（规划中）
    rag_chatbot/                RAG 问答机器人
    multi_agent_workflow/       多 Agent 工作流

04_papers_resources/    ← 论文与学习资源
    key_papers.md               精读论文笔记
    resources.md                推荐课程、工具、博客
```

---

## 01_llm_basics 内容详解

### 📘 01 · Transformer 架构全面解析

从「为什么 RNN 不够好」出发，完整构建一个可运行的 Mini-GPT。

**覆盖内容：**
- RNN 的长距离依赖退化 & 无法并行两大缺陷
- 完整文本处理流水线：Token ID → Embedding → 位置编码 → Transformer Block → 输出
- **位置编码**：正弦公式推导、频率设计原理、余弦相似度验证、RoPE 简介
- **自注意力**：QKV 的语义含义、缩放点积推导（为什么除以√d_k）、数值示例
- **因果掩码**：训练时防止「偷看未来」的实现原理
- **多头注意力**：8 个头的注意力权重热力图可视化
- **FFN**：4× 中间层的设计原理，ReLU vs GeLU vs SwiGLU 对比
- **Layer Normalization**：Pre-LN vs Post-LN，对比 Batch Norm
- **残差连接**：梯度流动可视化，深层网络为何离不开残差
- **完整 Decoder Block**：用 NumPy 手写，组装以上所有组件
- **Mini-GPT**：堆叠 N 层，实现贪心 / 温度 / Top-k / Top-p 自回归生成
- **训练目标**：交叉熵损失、困惑度（Perplexity）的直觉解释
- **GPT 系列规模演变**：GPT-2 Small 到 LLaMA-3.1 的参数统计

---

### 📘 02 · 分词（Tokenization）与词嵌入

搞清楚文本到数字的完整变换，以及为什么中文 API 调用比英文贵。

**覆盖内容：**
- 字符级 / 词级 / 子词级三种方案的取舍，序列长度对比可视化
- **BPE 算法从零实现**：初始词表构建、高频对统计、合并历史可视化
- **字节级 BPE**：UTF-8 字节编码图解，为什么任意语言 emoji 都能处理
- 不同字符类型的字节数对比（英文1字节 / 中文3字节 / emoji 4字节）
- **tiktoken 实战**：分词细节查看、中英文效率对比、各模型词表大小
- **Token 成本计算**：主流模型定价表、场景成本估算、5个节省成本技巧
- **上下文窗口**：从 16K 到 1M，超限检测工具
- **词嵌入原理**：查找表 = 可训练矩阵，语义关系的向量几何表达
- king - man + woman ≈ queen 的 2D 可视化 + 余弦相似度矩阵

---

### 📘 03 · Prompt Engineering 完全指南

同一个模型，好的 Prompt 和差的 Prompt 能产生天壤之别的效果。

**覆盖内容：**
- **LLM 如何看你的 Prompt**：消息拼接成长字符串，输出是概率采样
- **Zero-shot**：模糊 vs 精确 Prompt 的对比实验，多任务演示
- **Few-shot**：情感分类（带细分类别）、JSON 格式提取示例
- **Chain-of-Thought（CoT）**：为什么有效（token 数 = 思考空间），魔法短语触发
- **Self-Consistency**：多路径采样 + 投票，数学题准确率对比
- **System Prompt 设计**：同一问题在不同角色下的输出差异，代码审查助手实战
- **结构化输出**：JSON 模式 vs XML 标签，Claude 擅长 XML 的原因
- **温度与采样**：softmax 缩放原理可视化，Top-k vs Top-p 对比图
- **Prompt Injection**：三个版本的防御实现（无防御 / XML 隔离 / System 分离）
- **反模式清单**：7 个常见错误写法 + 改进对比

---

### 📘 04 · RAG 检索增强生成

解决 LLM 知识截止日期和幻觉问题的核心技术，企业 AI 落地必学。

**覆盖内容：**
- **幻觉问题演示**：同一个问题，纯 LLM 幻觉 vs RAG 有据可查的对比
- **RAG 完整流水线**：索引阶段（切块→向量化→存储）+ 查询阶段（检索→生成）
- **四种切块策略**：固定长度 / 句子 / 段落 / 递归，chunk 大小分布可视化
- **向量嵌入**：本地 sentence-transformers（无需 GPU/API Key），语义相似度矩阵
- **ChromaDB 实战**：创建集合、批量入库、相似度查询
- **BM25 从零实现**：TF-IDF 原理、k1/b 参数含义、中文字符级分词
- **混合检索**：BM25 + 向量搜索，RRF 倒数排名融合算法
- **LLM 重排序**：让模型评判候选 chunk 的相关性
- **RAG 评估**：忠实性 / 上下文相关性 / 答案相关性三指标，LLM-as-judge
- **失败模式分析**：4 种常见问题 + 改进方向，高级 RAG 技术一览

---

## 快速开始

### 环境配置

```bash
# 克隆仓库
git clone https://github.com/yuansunshun/llm-agents-cookbook.git
cd llm-agents-cookbook

# 安装依赖
pip install -r requirements.txt

# 配置 API Key（只有 03_prompting 和 04_rag 的生成部分需要）
cp .env.example .env
# 编辑 .env，填入你的 ANTHROPIC_API_KEY
```

### 启动 Jupyter

```bash
jupyter lab
```

### 学习顺序

```
如果你是 LLM 新手：
  01_transformer_arch → 02_tokenization → 03_prompting → 04_rag_intro

如果你已了解基础，想直接上手：
  03_prompting → 04_rag_intro → 02_agents_frameworks/（即将推出）
```

---

## 各模块依赖

| Notebook | 额外依赖 | 是否需要 API Key |
|----------|---------|----------------|
| 01_transformer_arch | `torch` | ❌ 不需要 |
| 02_tokenization | `tiktoken` | ❌ 不需要 |
| 03_prompting | `anthropic`, `python-dotenv` | ✅ ANTHROPIC_API_KEY |
| 04_rag_intro | `sentence-transformers`, `chromadb`, `anthropic` | ⚠️ 生成部分需要 |

---

## 规划中的内容

### 02 · Agents 框架实践

- **LangChain**：Chain、Agent、Tool、Memory 核心概念，RAG pipeline 搭建
- **LlamaIndex**：文档索引、Query Engine、多文档问答
- **AutoGen**：多 Agent 协作框架，角色分工与任务分解
- **Claude Agent SDK**：工具调用、长对话管理、流式输出

### 03 · 完整项目

- **RAG 问答机器人**：支持 PDF/Word 上传，多轮对话，引用来源
- **多 Agent 工作流**：研究员 + 编写者 + 审稿者协作，自动生成报告

---

## 贡献指南

欢迎 PR！提交前请确保：
- Notebook 在干净的 Python 环境中可完整运行
- 代码有充分的注释（但不要过度注释）
- 新增内容符合「讲清楚+可视化+可运行」的标准

---

## License

MIT

---

*如果这个仓库对你有帮助，欢迎 ⭐ Star！*
