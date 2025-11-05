# Inicialização

### Instale o UV
```
uv sync
```

### Inicialize o fastAPI com UV
```
uv run uvicorn app.main:app --reload
```

### Para instalar biblioteca no UV use
```
EX: uv add fastapi
```

### Inicializar banco
```
docker run -d --name postgres_jpa -e POSTGRES_USER=root -e POSTGRES_PASSWORD=SenhaForte123 -e POSTGRES_DB=jpa -p 5432:5432 postgres:15
```