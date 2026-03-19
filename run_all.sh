python scripts/run_pipeline.py

if [ ! -f output/summary.md ]; then
  echo "❌ summary.md が生成されていません"
  exit 1
fi

rclone copy output/summary.md gdrive:引き継ぎ
