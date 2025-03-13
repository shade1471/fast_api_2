import os
from datetime import datetime
from http import HTTPStatus
from typing import Union
from urllib.parse import urlparse

import dotenv
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi_pagination import Page, paginate, add_pagination

from data import users_data, support_data
from models.app import AppStatus
from models.user import UserResponse, UserData, UserCreateResponse, UserCreateData, UserUpdatedResponse

dotenv.load_dotenv()

app = FastAPI()
add_pagination(app)


@app.get("/api/users/", response_model=Page[UserData], status_code=HTTPStatus.OK)
async def get_users() -> Page[UserData]:
    users = list(users_data.values())
    return paginate(users)


@app.get("/api/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int) -> Union[UserResponse, JSONResponse]:
    try:
        user_data = users_data[user_id]
    except KeyError:
        return JSONResponse(status_code=HTTPStatus.NOT_FOUND, content={})
    return UserResponse(data=user_data, support=support_data)


@app.post("/api/users/", response_model=UserCreateResponse)
async def create_user(user: UserCreateData) -> UserCreateResponse:
    current_id = max(users_data.keys()) + 1
    formatted_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    users_data[current_id] = UserData(id=current_id, email='', first_name=user.name, last_name='', avatar='',
                                      job=user.job)
    return UserCreateResponse(name=user.name, job=user.job, id=str(current_id), createdAt=formatted_date)


@app.put("/api/users/{user_id}", response_model=UserUpdatedResponse)
async def update_user(user_id: int, user: UserCreateData) -> Union[UserUpdatedResponse, JSONResponse]:
    try:
        exist_user = users_data[user_id]
    except KeyError:
        return JSONResponse(status_code=HTTPStatus.NOT_FOUND, content={})
    users_data[user_id] = UserData(id=exist_user.id,
                                   email=exist_user.email,
                                   first_name=user.name,
                                   last_name=exist_user.last_name,
                                   avatar=exist_user.avatar,
                                   job=user.job)
    formatted_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    return UserUpdatedResponse(name=user.name, job=user.job, updatedAt=formatted_date)


@app.delete("/api/users/{user_id}")
async def delete_user(user_id: int) -> JSONResponse:
    try:
        del users_data[user_id]
    except KeyError:
        return JSONResponse(status_code=HTTPStatus.NOT_FOUND, content={})
    return JSONResponse(status_code=HTTPStatus.NO_CONTENT, content=None)


@app.get('/status', response_model=AppStatus, status_code=HTTPStatus.OK)
async def status() -> AppStatus:
    return AppStatus(database=bool(users_list), status='App run successful')


if __name__ == "__main__":
    import uvicorn

    users_list = list(users_data.values())
    for user in users_list:
        UserData.model_validate(user)

    parsed_app_url = urlparse(os.getenv('APP_URL'))
    uvicorn.run(app, host=parsed_app_url.hostname, port=parsed_app_url.port)
