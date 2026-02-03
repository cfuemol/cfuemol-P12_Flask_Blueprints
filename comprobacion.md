## ❓ ¿Qué puerto usa Gunicorn?

**8000**

---

## 🌐 ¿Qué hace `nginx_app.conf`?

Redirige todas las peticiones HTTP hacia **Gunicorn** en el servicio `web`.

---

## 📄 ¿Dónde se escriben los logs?

En el archivo:

```bash
logs/app.log
```

---

## 🧩 ¿Para qué sirve `wsgi.py`?

Sirve para exponer la aplicación **Flask** a **Gunicorn**, permitiendo que actúe como servidor WSGI.