from fastapi import FastAPI
from app.api.user_routes import router as UserRouter 
from app.db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(UserRouter)