# Post New Art
Generate new art and post to X

新しいアートを生成し、Xに投稿する


## Usage
1. Set up environment variables

```bash
cp .env.example .env
```

1. Start containers

```bash
docker compose up
```

3. Generate new art
```bash
curl -X POST http://localhost:8000/generate-art -H "Content-Type: application/json" -d '{"prompt": "a beautiful landscape"}'
```


