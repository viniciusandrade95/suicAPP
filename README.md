## Dia 2 — Configuração base + DB (Postgres no Neon)

Este projeto usa Flask + SQLAlchemy com migrations via Flask-Migrate, conectando
ao Postgres do Neon com `sslmode=require`.

### Configuração do `.env`

Crie um arquivo `.env` na raiz do projeto (veja o exemplo abaixo) e preencha
com a connection string do Neon:

```
DATABASE_URL=postgresql://USER:PASSWORD@HOST/DB?sslmode=require
SECRET_KEY=troque-por-uma-chave-segura
DB_POOL_SIZE=5
DB_MAX_OVERFLOW=10
```

> Observação: caso a connection string venha sem `sslmode=require`, o app
> adiciona automaticamente esse parâmetro.

### Inicialização local

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
flask --app run.py db upgrade
flask --app run.py run
```

### Teste de conectividade/latência

Com o app rodando:

```
curl http://localhost:5000/health/db
```
