import json
import os

INPUT_JSON = "input/final.json"
OUTPUT_MD = "output/summary.md"

def generate_md():
    if not os.path.exists(INPUT_JSON):
        print("❌ final.json が見つからない")
        return

    with open(INPUT_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)

    content = data.get("content", "")

    os.makedirs("output", exist_ok=True)

    # 既存ファイル削除
    if os.path.exists(OUTPUT_MD):
        os.remove(OUTPUT_MD)

    with open(OUTPUT_MD, "w", encoding="utf-8") as f:
        f.write(content)

    print("✅ Markdown生成完了:", OUTPUT_MD)


if __name__ == "__main__":
    generate_md()
