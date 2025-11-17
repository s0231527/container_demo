# Container Demo: FastAPI + React + Kafka (starter)

This is a minimal starter project to practice containerization, local development with `docker-compose`, and CI with GitHub Actions.

Structure:
- `api/` - FastAPI backend (Python 3.12). Has a simple endpoint and pytest tests.
- `frontend/` - Minimal React + Vite app (TypeScript). Simple component and test.
- `docker-compose.yml` - Bring up api, frontend, and Kafka (bitnami image) for local dev.
- `.github/workflows/ci.yml` - CI pipeline: build images and run tests.

**How to use**
1. Install Docker Desktop.
2. Build & run locally:
   ```bash
   docker-compose up --build
   ```
   - API: http://localhost:8000
   - Frontend: http://localhost:3000

3. Build images locally:
   ```bash
   docker build -t container-demo-api ./api
   docker build -t container-demo-frontend ./frontend
   ```

4. Run tests locally:
   - API: `docker run --rm container-demo-api pytest`
   - Frontend: run tests with Node locally (see frontend/README)

This repo is intentionally minimal so you can extend it:
- add Kafka producers/consumers,
- add CI deployment to a registry,
- add Kubernetes manifests.

