from fastapi import FastAPI

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


@app.get("/user/{first_name}/{last_name}") # В адресной строке вводитя /user/Имя/Фамилия
async def news(first_name: str, last_name: str) -> dict:
    return {'message': f'Hello, {first_name} {last_name}'}



