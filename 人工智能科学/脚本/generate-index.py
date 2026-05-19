#!/usr/bin/env python3
"""
从 YAML 前置元数据生成机器可读 JSON 索引。
用于 V39 搜索系统和 V40 知识图谱。
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "metadata-index.json"

ALL_FIELDS = ["title", "layer", "tags", "prerequisites", "see-also", "status", "last-updated"]


def parse_frontmatter(filepath):
    """Extract YAML frontmatter fields from a markdown file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    m = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not m:
        return None

    yaml_block = m.group(1)
    frontmatter = {}
    current_list_key = None

    for line in yaml_block.split("\n"):
        list_m = re.match(r'^\s*-\s*(.*)', line)
        if list_m and current_list_key:
            if current_list_key not in frontmatter:
                frontmatter[current_list_key] = []
            frontmatter[current_list_key].append(list_m.group(1).strip())
            continue

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


def collect_all_files():
    """Collect all .md files with their metadata."""
    entries = []

    # All layer directories
    for layer_dir in sorted(ROOT.iterdir()):
        if not layer_dir.is_dir() or layer_dir.name.startswith(".") or layer_dir.name == "scripts":
            continue
        for md_file in sorted(layer_dir.rglob("*.md")):
            if ".git" in md_file.parts:
                continue
            rel_path = str(md_file.relative_to(ROOT)).replace("\\", "/")
            meta = parse_frontmatter(md_file)
            if meta:
                entry = {"path": rel_path}
                for field in ALL_FIELDS:
                    value = meta.get(field)
                    if isinstance(value, list):
                        entry[field] = value
                    elif value is not None:
                        entry[field] = value
                    else:
                        entry[field] = [] if field in ("tags", "prerequisites", "see-also") else ""
                entries.append(entry)
            else:
                # Fallback for files without frontmatter
                entries.append({
                    "path": rel_path,
                    "title": md_file.stem,
                    "layer": layer_dir.name,
                    "tags": [],
                    "prerequisites": [],
                    "see-also": [],
                    "status": "unknown",
                    "last-updated": "",
                })

    # Root-level files
    for md_file in sorted(ROOT.glob("*.md")):
        if md_file.name == "metadata-baseline.md":
            continue
        rel_path = md_file.name
        meta = parse_frontmatter(md_file)
        if meta:
            entry = {"path": rel_path}
            for field in ALL_FIELDS:
                value = meta.get(field)
                if isinstance(value, list):
                    entry[field] = value
                elif value is not None:
                    entry[field] = value
                else:
                    entry[field] = [] if field in ("tags", "prerequisites", "see-also") else ""
            entries.append(entry)
        else:
            entries.append({
                "path": rel_path,
                "title": md_file.stem,
                "layer": "root",
                "tags": [],
                "prerequisites": [],
                "see-also": [],
                "status": "unknown",
                "last-updated": "",
            })

    return entries


def main():
    entries = collect_all_files()
    
    index = {
        "version": "V38",
        "generated": __import__("datetime").datetime.now().strftime("%Y-%m-%d %H:%M"),
        "total_files": len(entries),
        "files": entries,
    }

    # Per-layer stats
    layer_counts = {}
    for e in entries:
        layer = e.get("layer", "unknown")
        layer_counts[layer] = layer_counts.get(layer, 0) + 1
    index["layer_stats"] = {k: v for k, v in sorted(layer_counts.items())}

    # Status distribution
    status_counts = {}
    for e in entries:
        s = e.get("status", "unknown")
        status_counts[s] = status_counts.get(s, 0) + 1
    index["status_stats"] = dict(sorted(status_counts.items(), key=lambda x: -x[1]))

    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)

    print(f"JSON 索引已生成: {OUTPUT}")
    print(f"  文件总数: {index['total_files']}")
    print(f"  层统计: {json.dumps(index['layer_stats'], ensure_ascii=False)}")
    print(f"  状态统计: {json.dumps(index['status_stats'], ensure_ascii=False)}")


if __name__ == "__main__":
    main()
