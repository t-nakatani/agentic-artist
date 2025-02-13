FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*


COPY pyproject.toml uv.lock ./
RUN python -m pip install --no-cache-dir --upgrade pip && \
    python -m pip install --no-cache-dir uv && \
    uv pip install --system . && \
    uvx playwright install --with-deps --only-shell


COPY app app/
COPY main.py index.py ./

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/home/appuser/.local/bin:$PATH" \
    PYTHONPATH="/app"

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD python -c "import http.client; conn = http.client.HTTPConnection('localhost:8000'); conn.request('GET', '/'); response = conn.getresponse(); exit(0) if response.status == 200 else exit(1)"

CMD ["uv", "run", "uvicorn", "index:app", "--host", "0.0.0.0", "--port", "8000"]
