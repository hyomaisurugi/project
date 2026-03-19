import json

with open("data/input.json", "r", encoding="utf-8") as f:
    data = json.load(f)

filename = data["filename"]
content = data["content"]

# front matter 追加（統合用）
front_matter = f"""---
thread_group: {data.get("thread_group", "unknown")}
thread_part: {data.get("thread_part", 0)}
---

"""

with open(filename, "w", encoding="utf-8") as f:
    f.write(front_matter + content)

print(f"Generated: {filename}")
