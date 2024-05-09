from operator import attrgetter
from typing import List

from fastapi import APIRouter, HTTPException

from data import db_users
from models import User

user_router = APIRouter(prefix="/users", tags=["Users"])


# Получить пользователей, в количестве limit, начиная с offset,
# предварительно отсортированных по атрибуту sort_by и в порядке reverse
@user_router.get("", response_model=List[User])
async def get_users(sort_by: str = None,
                    reverse: bool = False,
                    limit: int = 10,
                    offset: int = 0) -> List[User]:
    if len(db_users) == 0:
        raise HTTPException(status_code=404, detail="Список пользователей пуст")
    if sort_by is None:
        sort_users = db_users
    else:
        sort_users = sorted(db_users, key=attrgetter(sort_by), reverse=reverse)
    return sort_users[offset:][:limit]


# Получить пользователя по его ID
@user_router.get("/{user_id}", response_model=User)
async def get_user(user_id: int) -> User:
    user = next((user for user in db_users if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return user


# Создать нового пользователя
@user_router.post(path="/", response_model=User)
async def create_user(user: User) -> User:
    db_users.append(user)
    return user


# Удаление пользователя по его ID
@user_router.delete("/{user_id}", response_model=User)
async def delete_user(user_id: int):
    user_index = next((i for i, u in enumerate(db_users) if u.id == user_id), None)
    if user_index is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    deleted_user = db_users.pop(user_index)
    return deleted_user


# Изменеие атрибутов пользователя по его ID
@user_router.put(path="/{user_id}", response_model=User)
async def update_user(user_id: int, user: User) -> User:
    user_index = next((i for i, us in enumerate(db_users) if us.id == user_id), None)
    if user_index is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    db_users[user_index].username = user.username
    db_users[user_index].wallet = user.wallet
    db_users[user_index].birthdate = user.birthdate
    return db_users[user_index]
