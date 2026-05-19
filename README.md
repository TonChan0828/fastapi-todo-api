# FastAPI Todo API

FastAPIの学習用プロジェクトです。

## 目的

認証付きTodo APIを題材に、FastAPIで実務レベルのAPIを設計・実装・テスト・Docker化・デプロイ方針の整理まで学習します。

## 技術スタック

- Python 3.12+
- FastAPI
- uv
- PostgreSQL
- SQLAlchemy
- Alembic
- Pydantic
- pytest
- Docker / Docker Compose
- GitHub Actions

## API予定

- GET /health
- POST /auth/signup
- POST /auth/login
- GET /auth/me
- GET /todos
- POST /todos
- GET /todos/{todo_id}
- PATCH /todos/{todo_id}
- DELETE /todos/{todo_id}