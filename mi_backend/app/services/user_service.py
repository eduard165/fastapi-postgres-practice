from app.models.user_model import User
from app.db.database import SessionLocal
from app.schemas.user_schema import UserCreate


def get_users():
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return users

def get_user_by_id(user_id: int):
    db = SessionLocal()
    user = db.query(User).filter(User.id_cliente == user_id).first()
    db.close()
    return user

def filter_users_by_name(name: str):
    db = SessionLocal()
    users = db.query(User).filter(User.nombre.ilike(f"%{name}%")).all()
    db.close()
    return users

def create_user(user: UserCreate):
    db = SessionLocal()
    new_user = User(nombre=user.nombre, correo=user.correo, telefono=user.telefono)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()
    return new_user

def update_user(user_id: int, user: UserCreate):
    db = SessionLocal()
    existing_user = db.query(User).filter(User.id_cliente == user_id).first()
    if not existing_user:
        db.close()
        return None
    existing_user.nombre = user.nombre
    existing_user.correo = user.correo
    existing_user.telefono = user.telefono
    db.commit()
    db.refresh(existing_user)
    db.close()
    return existing_user

def delete_user(user_id: int):
    db = SessionLocal()
    user = db.query(User).filter(User.id_cliente == user_id).first()
    if not user:
        db.close()
        return None
    db.delete(user)
    db.commit()
    db.close()
    return user