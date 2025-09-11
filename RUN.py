import os
import re

CATEGORIES = ["Easy", "Medium", "Hard"]
OUTPUT_FILE = "leetcode_index.md"

def parse_filename(filename):
    match = re.match(r"(\d+)\.(.+)\.md", filename)
    if match:
        number, title = match.groups()
        title = title.replace('_', ' ')
        return int(number), f"{number}. {title}"
    return None

def generate_section(category):
    dir_path = category  # 修正：直接使用相對路徑
    if not os.path.isdir(dir_path):
        return ""

    files = [f for f in os.listdir(dir_path) if f.endswith(".md")]
    files = sorted([f for f in files if re.match(r"\d+\..+\.md", f)])
    links = []
    for f in files:
        info = parse_filename(f)
        if info:
            _, title = info
            url = f"https://github.com/Hotshot824/Leetcode/blob/main/{category}/{f}"
            links.append(f"- [{title}]({url})")

    if links:
        return f"### {category}\n" + "\n".join(links) + "\n"
    return ""

def generate_index():
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write('title: "Leetcode | Master Guide"\n')
        f.write("author: Benson Hsu\n")
        f.write("date: 1970-01-01\n")
        f.write("category: Jekyll\n")
        f.write("layout: post\n")
        f.write("tags: [leetcode, algorithm]\n")
        f.write("---\n\n")
        f.write("> Notes leetcode problem\n{: .block-tip }\n\n")
        f.write("> Reference: [leetcode-master], [Python-LeetCode 581]\n{: .block-tip }\n\n")
        f.write("[leetcode-master]: https://github.com/youngyangyang04/leetcode-master\n")
        f.write("[Python-LeetCode 581]: https://hackmd.io/@bangyewu/ryLbEED23/%2FAXR8NqGRQj2MLo6oCY7DGQ\n\n")

        for cat in CATEGORIES:
            section = generate_section(cat)
            if section:
                f.write(section + "\n")

if __name__ == "__main__":
    generate_index()
