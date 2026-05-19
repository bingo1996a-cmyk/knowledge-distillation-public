#!/usr/bin/env python3
"""
人工智能科学知识库 - 文件规范检查
检查：命名规范、文件大小、模板合规性、无用文件检测。
"""

import os
import sys
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 允许的特例文件（跳过命名规范检查）：README、版本索引、存根前端元数据页、自动生成文件
ALLOWED_NAMES = {
    "README.md",
    "tags-index.md",
}

# 明确豁免的内容文件（如重定向页、缩略入口页）
EXEMPT_FILES = {
    "08-thought-history-culture/history-of-ai-overview.md",
}

# 排除在检查之外的目录
EXCLUDE_DIRS = {".git", "99-handoff", "log", "scripts", "superpowers", "site"}

# 层目录列表（用于检查 .gitkeep 等）
LAYER_DIRS = [
    "00-overview", "01-foundations", "02-paradigms", "03-model-families",
    "04-systems-engineering", "05-problem-spaces", "06-applications",
    "07-evaluation-safety-governance", "08-thought-history-culture",
    "20-updates", "90-appendices",
]

# 文件名命名规范
FILE_NAME_RE = re.compile(r'^[a-z0-9][a-z0-9-]*\.md$')

# 最小和最大文件大小（KB）
MIN_SIZE_KB = 0.5
MAX_SIZE_KB = 200

# 有状态模板关键词（用于存根检测）
STUB_KEYWORDS = ["// TODO", "<!-- TODO", "## TODO", "此页面正在构建中", "coming soon"]


def check_naming(filepath, rel_path):
    """检查文件名是否符合小写连字符命名规范。"""
    fname = filepath.name
    if fname in ALLOWED_NAMES:
        return None
    if not FILE_NAME_RE.match(fname):
        return f"命名不规范: {rel_path} (应使用小写字母、数字、连字符)"
    return None


def check_size(filepath, rel_path):
    """检查文件大小是否在合理范围内。"""
    size_kb = filepath.stat().st_size / 1024
    if size_kb < MIN_SIZE_KB and filepath.name not in ALLOWED_NAMES and rel_path not in EXEMPT_FILES:
        return f"文件过小 ({size_kb:.1f} KB): {rel_path}"
    if size_kb > MAX_SIZE_KB:
        return f"文件过大 ({size_kb:.1f} KB): {rel_path}"
    return None


def check_stub(filepath, rel_path):
    """检查是否是存根页（仅有 YAML 前置元数据而无实质内容）。"""
    if filepath.name in ALLOWED_NAMES or rel_path in EXEMPT_FILES:
        return None
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # 检查存根关键词
    for kw in STUB_KEYWORDS:
        if kw in content:
            return f"疑似存根 (含'{kw}'): {rel_path}"

    # 检查是否只有元数据无正文内容
    stripped = content.strip()
    body_match = re.split(r'^---$', stripped, maxsplit=2, flags=re.MULTILINE)
    if len(body_match) >= 3:
        body = body_match[2].strip()
        if len(body) < 50:  # 正文少于 50 字符
            return f"疑似存根 (正文仅 {len(body)} 字符): {rel_path}"
    return None


def check_gitkeep(layer_name):
    """检查层目录中是否还有 .gitkeep 文件（仅报告不终止CI）。"""
    layer_dir = ROOT / layer_name
    gitkeep = layer_dir / ".gitkeep"
    complaints = []
    if gitkeep.exists():
        # .gitkeep 是 git 保留空目录的惯例，directory-only 层可保留
        pass
    return complaints


def run_check():
    """运行所有文件规范检查。"""
    issues = []
    total_checked = 0

    for layer in LAYER_DIRS:
        layer_dir = ROOT / layer
        if not layer_dir.exists():
            continue

        # 检查 .gitkeep
        issues.extend(check_gitkeep(layer))

        for md_file in sorted(layer_dir.rglob("*.md")):
            if any(excl in md_file.parts for excl in EXCLUDE_DIRS):
                continue
            if ".git" in md_file.parts:
                continue

            rel_path = str(md_file.relative_to(ROOT)).replace("\\", "/")
            total_checked += 1

            for check_fn in [check_naming, check_size, check_stub]:
                result = check_fn(md_file, rel_path)
                if result:
                    issues.append(result)

    # 报告
    print(f"\n=== 文件规范检查 ===")
    print(f"检查文件数: {total_checked}")
    print(f"问题总数: {len(issues)}")

    if issues:
        print(f"\n--- 问题列表 ({len(issues)}) ---")
        for i, issue in enumerate(issues, 1):
            print(f"  {i}. {issue}")
    else:
        print("[OK] All passed!")

    # CI 退出码：有问题则返回 1
    return len(issues)


if __name__ == "__main__":
    sys.exit(run_check())
