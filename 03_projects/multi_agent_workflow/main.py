"""
Multi-Agent Workflow — 研究员 + 编写者 + 审稿者
用法：python main.py "你的研究问题"
输出：report_<timestamp>.md
"""
import os
import sys
import argparse
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

try:
    import anthropic
except ImportError:
    print("请先安装依赖：pip install anthropic python-dotenv")
    sys.exit(1)

MODEL = "claude-sonnet-4-6"


def call_claude(system: str, user: str, client: anthropic.Anthropic, max_tokens: int = 800) -> str:
    response = client.messages.create(
        model=MODEL,
        max_tokens=max_tokens,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    return response.content[0].text


def researcher(topic: str, client: anthropic.Anthropic) -> str:
    print("🔍 Researcher：正在收集关键信息...")
    return call_claude(
        system=(
            "You are a research analyst. Given a topic, provide:\n"
            "1. 3-5 key facts or findings\n"
            "2. Current state of the field\n"
            "3. Main challenges or open questions\n"
            "Be factual and concise."
        ),
        user=f"Research topic: {topic}",
        client=client,
        max_tokens=600,
    )


def writer(topic: str, research: str, client: anthropic.Anthropic) -> str:
    print("✍️  Writer：正在撰写报告...")
    return call_claude(
        system=(
            "You are a technical writer. Given research notes, write a structured Markdown report with:\n"
            "# Title\n"
            "## Overview (2-3 sentences)\n"
            "## Key Findings (bullet points)\n"
            "## Challenges\n"
            "## Conclusion\n"
            "Be clear, engaging, and accurate."
        ),
        user=f"Topic: {topic}\n\nResearch notes:\n{research}",
        client=client,
        max_tokens=800,
    )


def reviewer(report: str, client: anthropic.Anthropic) -> tuple[bool, str]:
    print("📋 Reviewer：正在审阅报告...")
    feedback = call_claude(
        system=(
            "You are an editor reviewing a technical report. Check for:\n"
            "- Clarity and flow\n"
            "- Factual consistency\n"
            "- Missing important points\n"
            "Start with APPROVED if the report is good enough to publish, or REVISE if it needs changes.\n"
            "Then explain your decision in 2-3 sentences."
        ),
        user=f"Review this report:\n\n{report}",
        client=client,
        max_tokens=300,
    )
    approved = feedback.strip().startswith("APPROVED")
    return approved, feedback


def revise(topic: str, report: str, feedback: str, client: anthropic.Anthropic) -> str:
    print("🔄 Writer：根据反馈修订...")
    return call_claude(
        system="You are a technical writer. Revise the report based on the reviewer's feedback. Keep the Markdown structure.",
        user=f"Original report:\n{report}\n\nReviewer feedback:\n{feedback}\n\nTopic: {topic}",
        client=client,
        max_tokens=900,
    )


def run_workflow(topic: str, max_revisions: int = 2) -> str:
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("错误：请设置 ANTHROPIC_API_KEY 环境变量")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    print(f"\n{'='*50}")
    print(f"主题：{topic}")
    print(f"{'='*50}\n")

    # 阶段 1：研究
    research = researcher(topic, client)
    print(f"  研究完成（{len(research)} 字符）\n")

    # 阶段 2：撰写
    report = writer(topic, research, client)
    print(f"  初稿完成（{len(report)} 字符）\n")

    # 阶段 3：审阅与修订循环
    for i in range(max_revisions):
        approved, feedback = reviewer(report, client)
        if approved:
            print(f"  ✅ 审阅通过（第 {i+1} 轮）\n")
            break
        print(f"  需要修订（第 {i+1}/{max_revisions} 轮）\n")
        report = revise(topic, report, feedback, client)
    else:
        print("  已达最大修订次数，使用当前版本\n")

    # 保存报告
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"report_{timestamp}.md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"# Research Report: {topic}\n\n")
        f.write(f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n\n")
        f.write("---\n\n")
        f.write(report)

    print(f"报告已保存至：{output_file}")
    return report


def main():
    parser = argparse.ArgumentParser(description="Multi-Agent Research Workflow")
    parser.add_argument("topic", nargs="?", default="Large Language Models in Production")
    parser.add_argument("--max-revisions", type=int, default=2)
    args = parser.parse_args()

    run_workflow(args.topic, args.max_revisions)


if __name__ == "__main__":
    main()
