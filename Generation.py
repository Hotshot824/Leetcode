#!/usr/bin/env python3
# A simple script to generate a master outline markdown file for Leetcode problems
# by scanning markdown files under Easy/Medium/Hard folders.
import argparse, os, re, sys
from pathlib import Path
from collections import defaultdict
from datetime import datetime

FRONT_RE = re.compile(r'^---\s*(.*?)\s*---', re.S | re.M)
KV_RE = re.compile(r'^([^:]+):\s*(.*)$')

def parse_frontmatter(text):
    m = FRONT_RE.search(text)
    if not m:
        return {}
    fm_block = m.group(1)
    fm = {}
    for line in fm_block.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        kvm = KV_RE.match(line)
        if kvm:
            k = kvm.group(1).strip()
            v = kvm.group(2).strip()
            fm[k] = v
    return fm

def find_md_files(root):
    root = Path(root)
    files = []
    for p in root.rglob('*.md'):
        # skip backups
        if p.name.endswith('.bak'):
            continue
        parts = [pp.lower() for pp in p.parts]
        # include files under Easy/Medium/Hard folders (case-insensitive)
        if any(x in parts for x in ('easy','medium','hard')):
            files.append(p)
    return sorted(files)

def extract_number(title, path):
    if title:
        m = re.search(r'\b(\d{1,6})\b', title)
        if m:
            return int(m.group(1))
    m = re.search(r'\b(\d{1,6})\b', Path(path).stem)
    if m:
        return int(m.group(1))
    return None

def build_outline(files, repo_prefix=None):
    out = defaultdict(lambda: defaultdict(list))  # Category -> Subcategory -> list of (num, title, link)
    for p in files:
        try:
            txt = p.read_text(encoding='utf-8')
        except Exception:
            continue
        fm = parse_frontmatter(txt)
        title = fm.get('Title') or p.stem
        cat = fm.get('Category') or 'Other'
        sub = fm.get('Subcategory') or ''
        num = extract_number(title, p)
        display = title
        # stable relative path
        rel = os.path.relpath(p.resolve(), Path.cwd())
        if repo_prefix:
            link = repo_prefix.rstrip('/') + '/' + rel.replace('\\', '/')
        else:
            link = rel.replace('\\', '/')
        out[cat][sub].append((num if num is not None else 999999, display, link))
    # sort items by number then title
    for cat in out:
        for sub in out[cat]:
            out[cat][sub].sort(key=lambda x: (x[0], x[1]))
    return out

MASTER_HEADER = """---
title: "Leetcode | Master Guide"
author: Benson Hsu
date: 1970-01-01
category: Jekyll
layout: post
tags: [leetcode, algorithm]
---

> Notes leetcode problem 
{: .block-tip }

> Reference: [leetcode-master], [Python-LeetCode 581] 從基礎的 Array 到 Dynamic Programming 都有詳細的解釋。
{: .block-tip }

[leetcode-master]: https://github.com/youngyangyang04/leetcode-master
[Python-LeetCode 581]: https://hackmd.io/@bangyewu/ryLbEED23/%2FAXR8NqGRQj2MLo6oCY7DGQ

"""

def render_master(out):
    # ensure Other is last
    cats = sorted([c for c in out.keys() if c != 'Other']) + (['Other'] if 'Other' in out else [])
    lines = [MASTER_HEADER]
    for cat in cats:
        lines.append(f"### {cat}\n")
        for sub in sorted(out[cat].keys(), key=lambda s: (s == '', s.lower())):
            items = out[cat][sub]
            if sub:
                lines.append(f"**{sub}**  ")
            for _, title, link in items:
                lines.append(f"[{title}]({link})  ")
            lines.append("")  # blank line between subgroups
    # Add timestamp and last edit info
    ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    lines.append("> ##### Last Edit\n> %s %s\n{: .block-tip }\n" % (Path.cwd().name, ts))
    return '\n'.join(lines)

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--root', default='.', help='repo root to scan (default: .)')
    p.add_argument('--output', default='1970-01-01-leetcode_guide.md', help='output markdown file')
    p.add_argument('--dry-run', action='store_true', help='only list matched files')
    p.add_argument('--repo-prefix', default='https://github.com/Hotshot824/Leetcode/blob/publish',
                   help='optional GitHub repo prefix for links')
    p.add_argument('--stdout', action='store_true', help='print output to stdout instead of file')
    args = p.parse_args()

    files = find_md_files(args.root)
    if args.dry_run:
        for f in files:
            print(f)
        print("Total:", len(files))
        return

    out = build_outline(files, repo_prefix=args.repo_prefix)
    content = render_master(out)

    # Output to file or stdout.
    if args.stdout:
        sys.stdout.write(content)
    else:
        Path(args.output).write_text(content, encoding='utf-8')
        print("Wrote", args.output)

if __name__ == '__main__':
    main()