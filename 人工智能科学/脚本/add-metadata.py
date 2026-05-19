#!/usr/bin/env python3
"""
批量 YAML 前置元数据添加脚本。
为知识库中缺少元数据的 .md 文件添加基础模板，
自动推断 title（从一级标题）、layer（从目录路径）、status（默认 stable）。
tags、prerequisites、see-also 留空供手动填充。
"""

import os
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 层标识映射
LAYER_MAP = {
    "00-overview": "00-overview",
    "01-foundations": "01-foundations",
    "02-paradigms": "02-paradigms",
    "03-model-families": "03-model-families",
    "04-systems-engineering": "04-systems-engineering",
    "05-problem-spaces": "05-problem-spaces",
    "06-applications": "06-applications",
    "07-evaluation-safety-governance": "07-evaluation-safety-governance",
    "08-thought-history-culture": "08-thought-history-culture",
    "20-updates": "20-updates",
    "90-appendices": "90-appendices",
    "docs": "docs",
    "99-handoff": "99-handoff",
    "log": "log",
}

# 层 → 默认标签
LAYER_DEFAULT_TAG = {
    "00-overview": "evaluation",
    "01-foundations": "ai-theory",
    "02-paradigms": "machine-learning",
    "03-model-families": "machine-learning",
    "04-systems-engineering": "systems-engineering",
    "05-problem-spaces": "machine-learning",
    "06-applications": "ai-applications",
    "07-evaluation-safety-governance": "ai-safety",
    "08-thought-history-culture": "ai-history",
    "20-updates": "evaluation",
    "90-appendices": "evaluation",
    "docs": "evaluation",
    "99-handoff": "evaluation",
    "log": "evaluation",
}

TODAY = datetime.now().strftime("%Y-%m-%d")


def has_frontmatter(content):
    return content.startswith("---") and re.match(r'^---\s*\n', content)


def extract_title(content):
    """Extract first h1 heading from markdown content."""
    m = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return None


def detect_layer(rel_path):
    """Detect layer from relative file path."""
    parts = rel_path.split("/")
    if len(parts) >= 1:
        top_dir = parts[0]
        if top_dir in LAYER_MAP:
            return LAYER_MAP[top_dir]
    # Root-level files
    if len(parts) == 1:
        return "root"
    return "unknown"


def build_yaml_frontmatter(title, layer, default_tag):
    """Build YAML frontmatter string."""
    lines = ["---"]
    lines.append(f"title: {title}")
    lines.append(f"layer: {layer}")
    lines.append("tags:")
    lines.append(f"  - {default_tag}")
    lines.append("prerequisites: []")
    lines.append("see-also: []")
    lines.append("status: stable")
    lines.append(f"last-updated: {TODAY}")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def add_metadata(filepath, dry_run=False, force=False):
    """Add YAML frontmatter to a file if missing."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if has_frontmatter(content) and not force:
        return "skip_existing"

    # Compute relative path
    rel_path = str(filepath.relative_to(ROOT)).replace("\\", "/")

    # Extract title
    title = extract_title(content)
    if not title:
        title = filepath.stem  # fallback to filename

    # Detect layer
    layer = detect_layer(rel_path)
    default_tag = LAYER_DEFAULT_TAG.get(layer, "evaluation")

    # Build frontmatter
    fm = build_yaml_frontmatter(title, layer, default_tag)

    # Remove existing frontmatter if force
    if force and has_frontmatter(content):
        content = re.sub(r'^---\s*\n.*?\n---\s*\n*', '', content, count=1, flags=re.DOTALL)

    # Prepend frontmatter
    new_content = fm + content.lstrip("\n")

    if not dry_run:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

    return "added"


def process_layer(layer_name, dry_run=False, force=False):
    """Process all .md files in a layer directory."""
    layer_dir = ROOT / layer_name
    if not layer_dir.exists():
        print(f"  [跳过] 目录不存在: {layer_name}")
        return {"added": 0, "skipped": 0, "total": 0}

    results = {"added": 0, "skipped": 0, "total": 0}
    files = sorted(layer_dir.rglob("*.md"))
    
    for md_file in files:
        if ".git" in md_file.parts:
            continue
        results["total"] += 1
        status = add_metadata(md_file, dry_run=dry_run, force=force)
        if status == "added":
            results["added"] += 1
        else:
            results["skipped"] += 1

        if dry_run:
            rel = str(md_file.relative_to(ROOT)).replace("\\", "/")
            print(f"    {'[ADD]' if status == 'added' else '[SKIP]'} {rel}")

    return results


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Batch-add YAML frontmatter to knowledge base files")
    parser.add_argument("layers", nargs="*", help="Layer directories to process (default: all)")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    parser.add_argument("--force", action="store_true", help="Overwrite existing YAML frontmatter")
    
    args = parser.parse_args()
    
    layers = args.layers if args.layers else sorted(LAYER_MAP.keys())
    
    mode_str = "[DRY RUN]" if args.dry_run else "[EXECUTE]"
    print(f"\n{mode_str} 批量添加 YAML 前置元数据")
    print(f"目标层: {', '.join(layers)}\n")
    
    total_added = 0
    total_skipped = 0
    total_files = 0
    
    for layer in layers:
        print(f"  {layer}:")
        r = process_layer(layer, dry_run=args.dry_run, force=args.force)
        total_added += r["added"]
        total_skipped += r["skipped"]
        total_files += r["total"]
        action = "（预览，未写入）" if args.dry_run else ""
        print(f"    -> 添加: {r['added']}, 跳过: {r['skipped']}, 总数: {r['total']} {action}")
        print()
    
    print(f"=== 汇总 ===")
    print(f"  总文件: {total_files}")
    print(f"  已添加: {total_added}")
    print(f"  已跳过: {total_skipped}")
    if args.dry_run:
        print(f"\n  使用 python scripts/add-metadata.py 执行实际添加")


if __name__ == "__main__":
    main()
