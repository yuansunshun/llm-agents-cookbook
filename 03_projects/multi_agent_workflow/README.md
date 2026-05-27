# 多 Agent 工作流

演示多个专职 Agent 协同完成复杂任务。

## 工作流设计

```
用户输入任务
    ↓
规划 Agent — 将任务拆分为子步骤
    ↓
执行 Agent — 依次完成每个子步骤（可调用工具）
    ↓
审核 Agent — 验证结果，必要时反馈修正
    ↓
输出最终结果
```

## 快速开始

```bash
pip install -r ../../requirements.txt
python main.py
```
