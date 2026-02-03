# P12 - Flask Modular con Blueprints, Gunicorn, NGINX y Docker

## 🚀 Levantar el proyecto

Desde la raíz del proyecto:

```bash
docker compose up --build
```

## 🔌 Endpoints

### Página principal
👉 http://localhost:8080/

### Info del contenedor
👉 http://localhost:8080/info

Ping API
👉 http://localhost:8080/api/ping

```bash
{ "response": "pong" }
```


### Estado de la API
👉 http://localhost:8080/api/status

```bash
{ "status": "ok" }
```

### Items
👉 http://localhost:8080/api/items

```bash
["item1", "item2", "item3"]
```

## 🧪 Tests

Ejecutar los tests con:

```bash
pytest tests/test_api.py
```

## 📄 Logs

Los logs de la aplicación se guardan en:

```bash
logs/app.log
```
