# 模块二：Agents 框架与工具

## 学习目标

掌握主流 LLM Agents 框架的核心用法，能够构建工具调用、多轮对话、多智能体协作流程。

## 笔记列表

| 文件 | 框架 | 主题 |
|------|------|------|
| [01_langchain_basics.ipynb](01_langchain_basics.ipynb) | LangChain | Chain、Tools、Memory、LCEL |
| [02_llama_index_rag.ipynb](02_llama_index_rag.ipynb) | LlamaIndex | 文档加载、向量索引、查询引擎 |
| [03_autogen_multiagent.ipynb](03_autogen_multiagent.ipynb) | AutoGen | 多 Agent 对话、角色设定、人机协作 |
| [04_claude_agent_sdk.ipynb](04_claude_agent_sdk.ipynb) | Claude Agent SDK | Anthropic 工具调用、子 Agent、流式输出 |

## 框架对比

| 框架 | 适合场景 | 特点 |
|------|----------|------|
| LangChain | 复杂链路编排 | 生态丰富，组件多 |
| LlamaIndex | 知识库/RAG | 专注数据接入与检索 |
| AutoGen | 多 Agent 协作 | 对话驱动，灵活角色 |
| Claude SDK | Anthropic 生态 | 原生工具调用，简洁 |
