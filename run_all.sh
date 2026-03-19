#!/usr/bin/env bash

python scripts/run_pipeline.py

LATEST_FILE=$(ls -t output/*.md 2>/dev/null | head -n 1)

if [ -z "$LATEST_FILE" ]; then
  echo "❌ output に .md ファイルがありません"
  exit 1
fi

echo "✅ 最新Markdown: $LATEST_FILE"

rclone copy "$LATEST_FILE" gdrive:引き継ぎ
