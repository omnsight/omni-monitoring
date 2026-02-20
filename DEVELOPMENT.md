## Manage with uv

This project is managed with [uv](https://github.com/astral-sh/uv).

Install/Upgrade dependencies:
```bash
uv lock --upgrade
uv sync --extra dev
```

Clean up:
```bash
uv run poe clean
```

Run unit tests:
```bash
# loading .env is necessary for local testing
docker compose up -d --wait
export $(cat .env | xargs) && uv run pytest
docker compose down
```

Format the code using black:
```bash
uv run black .
uv run isort .
```

Run the application:
```bash
uv run uvicorn omni_monitoring.main:app --reload
```

## Run Service Locally & Debug

Run service:
```bash
docker-compose up -d --build --wait
docker compose down

docker inspect <container name>

docker logs <container name>
```

## Export OpenAPI Definition

Export the OpenAPI definition to `doc/openapi.json`:
```bash
uv run python scripts/export_openapi.py
```

## Setup Client

Located in `client/` directory.

Install client dependencies:
```bash
npm install
```

Generate client:
```bash
npm run generate
```

## Client Development

Run unit tests: 
```bash
docker compose up -d --wait
cd client && npm run pretest && npm run test && cd ..
docker compose down
```

Build the client:
```bash
npm run build
```
