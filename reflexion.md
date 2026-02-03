## 📘 ¿Qué he aprendido en esta práctica?

He aprendido a modularizar una aplicación Flask usando **Blueprints**, 
a configurar **Gunicorn** como servidor WSGI y a utilizar **NGINX** 
como proxy inverso dentro de un entorno con **Docker**.

---

## ⚠️ ¿Qué problemas encontré?

Al principio, el proxy **NGINX** no conectaba correctamente con **Gunicorn** 
debido a una configuración incorrecta del Dockerfile.

---

## ✅ ¿Cómo lo resolví?

Al ser un Dockerfile multietapa hay que copiar el PATH de referencia de gunicorn para que esté presente en el proyecto.
