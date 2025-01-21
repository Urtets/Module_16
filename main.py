from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {'message': 'Hello, World!'}


@app.get("/user/A/B")
async def news() -> dict:
    return {'message': f'Hello, Tester'}


@app.get("/id") # В адресной строке вводитя /id?username=Имя&age=Возраст
async def id_paginator(username: str = 'Uri', age: int = 24) -> dict:
    return {'user': username, 'Age': age}


@app.get("/user/{username}/{id}") # В адресной строке вводитя /user/Имя/Фамилия
async def news(username: Annotated[str, Path(min_length=3, max_length=15, description='Enter your username', example='Alex56')], # Annotated снимает обязательство вводить обязательные данные во второй параметр
               id: int) -> dict:
    return {'message': f'Hello, {username} {id}'}


# @app.get("/user/{username}/{id}") # В адресной строке вводитя /user/Имя/Фамилия
# async def news(username: str = Path(min_length=3, max_length=15, description='Enter your username', example='Alex56'),
#                id: int = Path(ge=0, le=100, description='Enter your id', example='75')) -> dict:
#     return {'message': f'Hello, {username} {id}'}



