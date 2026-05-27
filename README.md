# LLM & Agents 学习笔记

大语言模型与智能体（Agents）学习记录，以 Jupyter Notebook 为主要载体，涵盖原理、框架实践和完整项目。

## 学习路线

| 模块 | 内容 | 状态 |
|------|------|------|
| [01 · LLM 基础原理](01_llm_basics/) | Transformer、分词、Prompt Engineering、RAG | 🚧 进行中 |
| [02 · Agents 框架](02_agents_frameworks/) | LangChain、LlamaIndex、AutoGen、Claude SDK | 📝 规划中 |
| [03 · 实战项目](03_projects/) | RAG 问答机器人、多 Agent 工作流 | 📝 规划中 |
| [04 · 论文与资源](04_papers_resources/) | 精读论文笔记、学习资源汇总 | 📝 规划中 |

## 环境配置

```bash
# 克隆仓库
git clone https://github.com/<your-username>/agents-learning.git
cd agents-learning

# 创建虚拟环境（推荐）
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 启动 JupyterLab
jupyter lab
```

## API Key 配置

在项目根目录创建 `.env` 文件（已在 .gitignore 中，不会提交）：

```
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
```

在 Notebook 中加载：

```python
from dotenv import load_dotenv
load_dotenv()
```
