from typing import List, Annotated

from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    id: int = None
    username: str
    age: int = None


# zero_user = User()
# zero_user.id = 0
# zero_user.username = "Zero"
# zero_user.age = 0

users = []


@app.get('/users', response_model=List[User])
async def get_users() -> List[User]:
    return users


@app.post('/user/{username}/{age}', response_model=User)
async def post_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='Ivan34')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=24)]) -> User:
    user_len = len(users)
    user_id = 0
    if user_len == 0:
        user_id = 1
    else:
        user_id = users[user_len - 1].id + 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int) -> User:
    try:
        some_user = users[user_id - 1]
        some_user.username = username
        some_user.age = age
        users[user_id] = some_user
        return some_user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example=5)]):
    for i, user in enumerate(users):
        if user.id == user_id:
            return users.pop(i)
    raise HTTPException(status_code=404, detail="User was not found")
