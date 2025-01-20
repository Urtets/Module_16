from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def main_page():
    return "Главная страница"

@app.get('/user/admin')
async def admin_user():
    return "Вы вошли, как администратор"

@app.get('/user/{user_id}')
async def id_user(user_id: int):
    return f'Вы вошли как пользователь №{user_id}'

@app.get('/user')
async def address_line(username: str, age: int):
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'