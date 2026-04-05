from fastapi import APIRouter
from app.services.user_service import get_user_by_id, get_users, filter_users_by_name, create_user, update_user, delete_user
from app.schemas.user_schema import UserCreate

router = APIRouter()

@router.get("/users")
def read_users():
    return get_users()

@router.get("/users/search")
def search_users(nombre: str = None):
    if nombre:
        return filter_users_by_name(nombre)
    return get_users()

@router.post("/users")
def create_user_route(user: UserCreate):
    return create_user(user)

@router.get("/users/{user_id}")
def read_user(user_id: int):
    return get_user_by_id(user_id)

@router.delete("/users/{user_id}")
def delete_user_route(user_id: int):
    return delete_user(user_id)

@router.put("/users/{user_id}")
def update_user_route(user_id: int, user: UserCreate):
    return update_user(user_id, user)