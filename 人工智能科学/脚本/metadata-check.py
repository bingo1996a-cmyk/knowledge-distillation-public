#!/usr/bin/env python3
"""
人工智能科学知识库 - YAML 元数据完整性检查
扫描指定层的 .md 文件，检查 YAML 前置元数据完整性。
"""

import os
import re
import sys
import json
from datetime import datetime
from pathlib import Path

# 知识库根目录
ROOT = Path(__file__).resolve().parent.parent

# 层目录列表
LAYERS = [
    "00-overview", "01-foundations", "02-paradigms", "03-model-families",
    "04-systems-engineering", "05-problem-spaces", "06-applications",
    "07-evaluation-safety-governance", "08-thought-history-culture",
    "20-updates", "90-appendices", "docs",
]

REQUIRED_FIELDS = {"title", "layer", "tags", "status"}
ALL_FIELDS = {"title", "layer", "tags", "prerequisites", "see-also", "status", "last-updated"}

# 自动生成的文件（如 mkdocs tags 插件输出的索引页），跳过元数据检查
AUTO_GENERATED_FILES = {
    "90-appendices/tags-index.md",
}


def parse_frontmatter(filepath):
    """Extract YAML frontmatter fields from a markdown file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Match YAML between --- markers at the start of file
    m = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not m:
        return None

    yaml_block = m.group(1)
    frontmatter = {}
    current_list_key = None

    for line in yaml_block.split("\n"):
        # List item
        list_m = re.match(r'^\s*-\s*(.*)', line)
        if list_m and current_list_key:
            if current_list_key not in frontmatter:
                frontmatter[current_list_key] = []
            frontmatter[current_list_key].append(list_m.group(1).strip())
            continue

        # Key-value pair
        kv_m = re.match(r'^(\w[\w-]*):\s*(.*)', line)
        if kv_m:
            key = kv_m.group(1)
            value = kv_m.group(2).strip()
            if value == "" or value == "[]":
                frontmatter[key] = []
                current_list_key = key
            else:
                frontmatter[key] = value
                current_list_key = None
        else:
            current_list_key = None

    return frontmatter


def scan_layer(layer_name, root_dir=ROOT):
    """Scan all .md files in a layer directory."""
    layer_dir = root_dir / layer_name
    results = []

    if not layer_dir.exists():
        return results

    for md_file in sorted(layer_dir.rglob("*.md")):
        if ".git" in md_file.parts:
            continue
        rel_path = str(md_file.relative_to(root_dir)).replace("\\", "/")
        if rel_path in AUTO_GENERATED_FILES:
            continue
        size_kb = round(md_file.stat().st_size / 1024, 1)
        meta = parse_frontmatter(md_file)

        if meta is None:
            results.append({
                "file": rel_path,
                "size_kb": size_kb,
                "has_yaml": False,
                "missing_fields": list(REQUIRED_FIELDS),
                "status": "N/A",
            })
        else:
            missing = [f for f in REQUIRED_FIELDS if f not in meta or not meta.get(f)]
            status = meta.get("status", "N/A") if isinstance(meta.get("status"), str) else "N/A"
            results.append({
                "file": rel_path,
                "size_kb": size_kb,
                "has_yaml": True,
                "missing_fields": missing if missing else [],
                "status": status,
            })

    return results


def run_check(target_layer=None, report_file=None):
    """Run metadata check and optionally write report."""
    layers_to_check = [target_layer] if target_layer else LAYERS

    all_results = []
    for layer in layers_to_check:
        all_results.extend(scan_layer(layer))

    total = len(all_results)
    with_yaml = sum(1 for r in all_results if r["has_yaml"])
    without_yaml = total - with_yaml
    pct_yaml = round(with_yaml / total * 100, 1) if total > 0 else 0

    # Status distribution
    status_counts = {}
    for r in all_results:
        s = r["status"]
        status_counts[s] = status_counts.get(s, 0) + 1

    # ====== Console output ======
    print(f"\n=== 元数据完整性检查 ===")
    print(f"知识库根目录: {ROOT}")
    print(f"文件总数: {total}")
    print(f"有元数据: {with_yaml} ({pct_yaml}%)")
    print(f"无元数据: {without_yaml} ({100 - pct_yaml}%)")

    no_yaml_files = [r for r in all_results if not r["has_yaml"]]
    if no_yaml_files:
        print(f"\n--- 缺少元数据的文件 ({len(no_yaml_files)}) ---")
        for r in no_yaml_files:
            print(f"  {r['file']} ({r['size_kb']} KB)")

    field_missing = [r for r in all_results if r["has_yaml"] and r["missing_fields"]]
    if field_missing:
        print(f"\n--- 字段不完整的文件 ({len(field_missing)}) ---")
        for r in field_missing:
            print(f"  {r['file']} -- 缺失: {', '.join(r['missing_fields'])}")

    if status_counts:
        print(f"\n--- 状态分布 ---")
        for s, c in sorted(status_counts.items(), key=lambda x: -x[1]):
            print(f"  {s}: {c}")

    # ====== Report file ======
    if report_file:
        report_path = ROOT / report_file
        lines = [
            "# 元数据检查报告",
            "",
            f"检查时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            "",
            "## 总览",
            "",
            "| 指标 | 数值 |",
            "|------|------|",
            f"| 文件总数 | {total} |",
            f"| 有元数据 | {with_yaml} ({pct_yaml}%) |",
            f"| 无元数据 | {without_yaml} ({100 - pct_yaml}%) |",
            "",
        ]

        if no_yaml_files:
            lines += ["## 无元数据文件", "", "| 文件 | 大小 |", "|------|------|"]
            for r in no_yaml_files:
                lines.append(f"| {r['file']} | {r['size_kb']} KB |")
            lines.append("")

        if field_missing:
            lines += ["## 字段不完整的文件", "", "| 文件 | 缺失字段 |", "|------|---------|"]
            for r in field_missing:
                lines.append(f"| {r['file']} | {', '.join(r['missing_fields'])} |")
            lines.append("")

        if status_counts:
            lines += ["## 状态分布", "", "| 状态 | 数量 |", "|------|------|"]
            for s, c in sorted(status_counts.items(), key=lambda x: -x[1]):
                lines.append(f"| {s} | {c} |")
            lines.append("")

        with open(report_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")

        print(f"\n报告已保存: {report_path}")

    return all_results


if __name__ == "__main__":
    # Usage: python scripts/metadata-check.py [target_layer] [report_file]
    # If target_layer is "all" or omitted, scan all layers
    target = None
    report = "metadata-baseline.md"
    if len(sys.argv) > 1:
        arg1 = sys.argv[1].strip()
        if arg1 and arg1.lower() != "all":
            target = arg1
    if len(sys.argv) > 2:
        report = sys.argv[2].strip() or "metadata-baseline.md"
    run_check(target_layer=target, report_file=report)
