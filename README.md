# fastapi-postgres-practice

Repositorio de práctica para desarrollar **APIs con FastAPI** y **PostgreSQL**.  
Este proyecto sirve como laboratorio personal para aprender y experimentar con la creación de endpoints, manejo de bases de datos, y buenas prácticas en el desarrollo de backend con Python.

## 📌 Tecnologías

- **Python 3.11+**
- **FastAPI** – framework moderno para construir APIs rápidas.
- **PostgreSQL** – sistema de base de datos relacional.
- **SQLAlchemy** – ORM para interactuar con la base de datos.
- **Pydantic** – validación de datos y serialización.
- **Uvicorn** – servidor ASGI para correr la aplicación.


## 🛠 Estructura del proyecto

```text
mi_backend/
├── api/
│   └── user_routes.py        # Endpoints de usuarios
├── db/
│   └── database.py           # Configuración y conexión a PostgreSQL
├── models/
│   └── usr_model.py          # Modelos SQLAlchemy
├── schemas/
│   └── user_schema.py        # Esquemas Pydantic
├── services/
│   └── user_service.py       # Lógica de negocio / CRUD
├── main.py                   # Punto de entrada de FastAPI
