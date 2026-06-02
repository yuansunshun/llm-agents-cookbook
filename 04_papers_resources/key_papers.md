# 精读论文笔记

## Transformer 基础

### Attention Is All You Need (2017)
- **作者**：Vaswani et al.，Google Brain
- **核心贡献**：提出纯注意力机制的 Seq2Seq 架构，取代 RNN/CNN
- **关键公式**：$\text{Attention}(Q,K,V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$
- **关键洞察**：多头注意力允许模型同时关注不同位置的不同表示子空间；位置编码解决了序列顺序感知问题
- **对应章节**：`01_llm_basics/01_transformer_arch.ipynb`

---

### BERT: Pre-training of Deep Bidirectional Transformers (2018)
- **作者**：Devlin et al.，Google AI
- **核心贡献**：用双向 Transformer 做语言预训练，通过 Masked LM 和 Next Sentence Prediction 任务学到丰富语言表示
- **关键洞察**：双向上下文比单向 GPT 在理解任务（分类、NER、QA）上更有优势；「预训练 + 微调」范式成为 NLP 标准流程
- **对应章节**：`01_llm_basics/01_transformer_arch.ipynb`

---

### GPT-3: Language Models are Few-Shot Learners (2020)
- **作者**：Brown et al.，OpenAI
- **核心贡献**：1750 亿参数模型展示了 in-context learning——不需要梯度更新，仅靠几个示例就能完成新任务
- **关键洞察**：规模（scale）带来了质变，few-shot 能力随模型规模呈现涌现；prompt 设计的重要性首次系统性凸显
- **对应章节**：`01_llm_basics/03_prompting.ipynb`

---

## 对齐与指令微调

### InstructGPT: Training Language Models to Follow Instructions (2022)
- **作者**：Ouyang et al.，OpenAI
- **核心贡献**：用 RLHF（人类反馈强化学习）让 GPT-3 更好地遵循指令，对齐人类意图
- **关键洞察**：人类偏好数据比规模更重要——130 亿参数的 InstructGPT 被人类评为优于 1750 亿参数 GPT-3 的输出
- **对应章节**：`01_llm_basics/03_prompting.ipynb`

---

### Constitutional AI: Harmlessness from AI Feedback (2022)
- **作者**：Bai et al.，Anthropic
- **核心贡献**：用 AI 自身生成的批评和修订来训练更有益、无害的模型（RLAIF），减少对人工标注的依赖
- **关键洞察**：AI 可以用一组「宪法」原则自我评估和改进，无需大量有害样本的人工标注
- **对应章节**：`01_llm_basics/03_prompting.ipynb`、`02_agents_frameworks/04_claude_agent_sdk.ipynb`

---

## 高效微调

### LoRA: Low-Rank Adaptation of Large Language Models (2021)
- **作者**：Hu et al.，Microsoft
- **核心贡献**：通过在原权重矩阵旁注入低秩分解矩阵（A×B），用极少参数（<1%）实现接近全参数微调的效果
- **关键洞察**：预训练权重本质上是低秩的——任务适应只需要修改低维子空间，不必更新所有参数
- **对应章节**：`01_llm_basics/01_transformer_arch.ipynb`

---

## 推理增强

### Chain-of-Thought Prompting Elicits Reasoning (2022)
- **作者**：Wei et al.，Google Brain
- **核心贡献**：在提示中加入中间推理步骤示例，显著提升 LLM 在数学、逻辑推理任务上的表现
- **关键洞察**：只有足够大的模型（~100B 参数以上）才能从 CoT 中受益；思维链是模型内部推理能力的「激活」而非「注入」
- **对应章节**：`01_llm_basics/03_prompting.ipynb`

---

### Self-Consistency Improves Chain of Thought Reasoning (2023)
- **作者**：Wang et al.，Google Brain
- **核心贡献**：对同一问题生成多条推理路径，通过多数投票选出最终答案，提升 CoT 的可靠性
- **关键洞察**：推理不是唯一路径的，多路径后聚合比单路径贪心更稳健；temperature > 0 在推理任务中有正向作用
- **对应章节**：`01_llm_basics/03_prompting.ipynb`

---

### Tree of Thoughts: Deliberate Problem Solving with LLMs (2023)
- **作者**：Yao et al.，Princeton & Google
- **核心贡献**：让 LLM 像树搜索一样探索多个推理分支，支持回溯和前瞻，解决需要系统搜索的复杂问题
- **关键洞察**：CoT 是深度优先无回溯的；ToT 引入广度优先和 best-first 搜索，使 LLM 能解决 24 点游戏等组合问题
- **对应章节**：`02_agents_frameworks/`

---

## RAG

### Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (2020)
- **作者**：Lewis et al.，Facebook AI
- **核心贡献**：将检索模块与生成模型结合，解决 LLM 知识截止和幻觉问题
- **关键洞察**：检索到的文档作为「软知识」注入，比纯参数记忆更新更快、更可验证
- **对应章节**：`01_llm_basics/04_rag_intro.ipynb`、`02_agents_frameworks/02_llama_index_rag.ipynb`

---

## Agents

### ReAct: Synergizing Reasoning and Acting in Language Models (2022)
- **作者**：Yao et al.
- **核心贡献**：让 LLM 交替生成推理轨迹（Thought）和动作（Action），显著提升工具使用能力
- **关键洞察**：推理（Thought）帮助规划，行动（Action）获取外部信息，两者交替形成闭环比纯推理或纯行动更好
- **对应章节**：`02_agents_frameworks/01_langchain_basics.ipynb`

---

### AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation (2023)
- **作者**：Wu et al.，Microsoft
- **核心贡献**：通过可配置的对话式 Agent 框架，让多个 LLM Agent 相互通信协作完成复杂任务
- **关键洞察**：Agent 角色专一化（Coder/Critic/Tester）比单个全能 Agent 质量更高；Human-in-the-loop 可以在任意节点注入
- **对应章节**：`02_agents_frameworks/03_autogen_multiagent.ipynb`

---

> 持续更新中...
