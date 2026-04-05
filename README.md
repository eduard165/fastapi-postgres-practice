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
├── app/
│   ├── main.py          # Punto de entrada de FastAPI
│   ├── models.py        # Modelos SQLAlchemy / Pydantic
│   ├── crud.py          # Funciones de acceso a la base de datos
│   └── routers/         # Endpoints organizados
├── venv/                # Entorno virtual
├── .gitignore
├── requirements.txt
└── README.md
