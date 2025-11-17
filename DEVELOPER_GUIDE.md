# Developer Guide (minimal)

- Python version: 3.12
- Node version: 20
- Use docker-compose for local development: `docker-compose up --build`
- Tests:
  - API: pytest (in `api/`)
  - Frontend: run locally with Node
- CI: GitHub Actions configured in `.github/workflows/ci.yml`.
- Dockerfiles in `api/` and `frontend/` follow multi-stage/build best practices.
