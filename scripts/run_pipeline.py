import json
import os

INPUT_JSON = "input/final.json"
OUTPUT_DIR = "output"

def generate_md():
    if not os.path.exists(INPUT_JSON):
        print("❌ final.json が見つからない")
        return

    with open(INPUT_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)

    filename = data.get("filename", "summary.md")
    content = data.get("content", "")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    output_path = os.path.join(OUTPUT_DIR, filename)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    print("✅ Markdown生成完了:", output_path)

if __name__ == "__main__":
    generate_md()

if content.strip() == "..." or len(content.strip()) < 20:
    print("❌ content が短すぎます。JSONが省略されている可能性があります")
    return
