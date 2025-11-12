# Python FastAPI mirror of the Node Fastify app

This folder contains a FastAPI server that mirrors the endpoints and logic of the Node Fastify project in this repository.

Quick start

1. Create a virtual environment and install deps:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r src-python/requirements.txt
```

2. Run migrations (creates data directory and sqlite DB):

```bash
python src-python/db/init_db.py
```

3. Start the server:

```bash
uvicorn src-python.main:app --reload --port 3000
```

Endpoints

- GET /health
- GET /favorites
- GET /favorites/{id}
- POST /favorites { name }
- DELETE /favorites/{id}
- GET /characters?name={name}
- GET /rickandmorty?name={name}  (requires name query param)

Notes

- The app uses the same SQLite file location: `data/dev.sqlite` by default.
- The `db/init_db.py` script applies the same schema and trigger for timestamps.
