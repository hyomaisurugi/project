import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = ROOT / "input" / "input.json"
OUTPUT_DIR = ROOT / "output"

OUTPUT_DIR.mkdir(exist_ok=True)

with INPUT_FILE.open("r", encoding="utf-8") as f:
    data = json.load(f)

filename = data["filename"]
content = data["content"]

# front matter 追加（統合用）
front_matter = f"""---
thread_group: {data.get("thread_group", "unknown")}
thread_part: {data.get("thread_part", 0)}
---

"""

output_file = OUTPUT_DIR / filename

with output_file.open("w", encoding="utf-8") as f:
    f.write(front_matter + content)

print(f"Generated: {output_file}")
