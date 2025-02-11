# ビルドステージ
FROM python:3.12-slim

# 必要なビルドツールをインストール
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 作業ディレクトリを設定
WORKDIR /app

# 依存関係ファイルをコピー
COPY pyproject.toml uv.lock ./

# uvをインストールして依存関係をインストール
RUN python -m pip install --no-cache-dir --upgrade pip && \
    python -m pip install --no-cache-dir uv && \
    uv pip install --system . && \
    uvx playwright install --with-deps

# アプリケーションコードをコピー
COPY app app/
COPY main.py index.py ./

# 非rootユーザーを作成
RUN useradd -m appuser && \
    chown -R appuser:appuser /app
USER appuser

# 環境変数を設定
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/home/appuser/.local/bin:$PATH" \
    PYTHONPATH="/app"

# ヘルスチェック
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD python -c "import http.client; conn = http.client.HTTPConnection('localhost:8000'); conn.request('GET', '/'); response = conn.getresponse(); exit(0) if response.status == 200 else exit(1)"

# コンテナ起動時のコマンド
CMD ["uv", "run", "uvicorn", "index:app", "--host", "0.0.0.0", "--port", "8000"]
