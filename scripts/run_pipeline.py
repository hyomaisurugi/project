import json
import os
import sys

INPUT_JSON = "input/final.json"
OUTPUT_DIR = "output"


def validate_data(data: dict) -> tuple[bool, str]:
    if not isinstance(data, dict):
        return False, "JSONのルートがオブジェクトではありません"

    filename = data.get("filename")
    content = data.get("content")

    if not filename or not isinstance(filename, str):
        return False, "filename が存在しないか、不正です"

    if not filename.endswith(".md"):
        return False, "filename は .md で終わる必要があります"

    if "/" in filename or "\\" in filename:
        return False, "filename にパス区切り文字は使えません"

    if content is None or not isinstance(content, str):
        return False, "content が存在しないか、不正です"

    stripped = content.strip()

    if not stripped:
        return False, "content が空です"

    if stripped == "...":
        return False, "content が '...' のみです。省略されたJSONを貼った可能性があります"

    if len(stripped) < 20:
        return False, "content が短すぎます。JSONが不完全な可能性があります"

    return True, ""


def load_json(path: str) -> dict:
    if not os.path.exists(path):
        print(f"❌ {path} が見つかりません")
        sys.exit(1)

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ JSONの読み込みに失敗しました: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ ファイル読み込みに失敗しました: {e}")
        sys.exit(1)

    return data


def generate_md() -> str:
    data = load_json(INPUT_JSON)

    is_valid, error_message = validate_data(data)
    if not is_valid:
        print(f"❌ JSON検証エラー: {error_message}")
        sys.exit(1)

    filename = data["filename"]
    content = data["content"]

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    output_path = os.path.join(OUTPUT_DIR, filename)

    print(f"DEBUG filename: {filename}")
    print(f"DEBUG content head: {content[:80].replace(chr(10), ' ')}")

    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception as e:
        print(f"❌ Markdown書き込みに失敗しました: {e}")
        sys.exit(1)

    print(f"✅ Markdown生成完了: {output_path}")
    return output_path


if __name__ == "__main__":
    generate_md()
