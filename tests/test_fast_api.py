from http import HTTPStatus
from random import randint

import pytest
import requests
from data import users_data


class TestGetUser:

    @pytest.mark.parametrize('user_id', [1, 2, 3, 4, 5])
    def test_user_data(self, users_endpoint, user_id):
        response = requests.get(f"{users_endpoint}/{user_id}")
        assert response.status_code == HTTPStatus.OK
        body = response.json()
        data = body["data"]

        assert data["id"] == users_data[user_id].id
        assert data["email"] == users_data[user_id].email
        assert data["first_name"] == users_data[user_id].first_name
        assert data["last_name"] == users_data[user_id].last_name

    def test_response_when_user_not_exist(self, users_endpoint):
        rnd_id = randint(1000, 1999)
        response = requests.get(f"{users_endpoint}/{rnd_id}")
        assert response.status_code == HTTPStatus.NOT_FOUND
        body = response.json()
        assert not body


class TestCRUD:

    @pytest.mark.parametrize('user_dict', [
        {"name": "Max", "job": "qa-manual"},
        {'name': 'Alisa', 'job': 'qa-auto'}
    ])
    def test_create_user_post_request(self, users_endpoint, user_dict):
        response = requests.post(users_endpoint, json=user_dict)
        assert response.status_code == HTTPStatus.OK
        body = response.json()
        assert body['name'] == user_dict['name']
        assert body['job'] == user_dict['job']

    def test_update_exist_user(self, users_endpoint):
        new_user = {"name": "Kolya", "job": "PM"}
        new_data_user = {"name": "Nikolay", "job": "Super PM"}
        response = requests.post(users_endpoint, json=new_user)
        assert response.status_code == HTTPStatus.OK, 'Не удалось создать пользователя'
        current_id = response.json()['id']

        response_update = requests.put(f"{users_endpoint}/{current_id}", json=new_data_user)
        assert response_update.status_code == HTTPStatus.OK
        body = response_update.json()
        assert body['name'] == new_data_user['name']
        assert body['job'] == new_data_user['job']

        response_updated_user = requests.get(f"{users_endpoint}/{current_id}")
        assert response_updated_user.status_code == HTTPStatus.OK
        new_body = response_updated_user.json()
        data = new_body["data"]
        assert data['first_name'] == new_data_user["name"]
        assert data['job'] == new_data_user["job"]

    def test_update_not_exist_user(self, users_endpoint):
        new_data_user = {"name": "Maxim", "job": "driver"}
        user_id = 1000

        response_update = requests.put(f"{users_endpoint}/{user_id}", json=new_data_user)
        assert response_update.status_code == HTTPStatus.NOT_FOUND
        assert not response_update.json()

    def test_delete_user(self, users_endpoint):
        new_user = {"name": "Eraser", "job": "cleaner"}
        response = requests.post(users_endpoint, json=new_user)
        assert response.status_code == HTTPStatus.OK, 'Не удалось создать пользователя'
        current_id = response.json()['id']

        delete_response = requests.delete(f'{users_endpoint}/{current_id}')
        assert delete_response.status_code == HTTPStatus.NO_CONTENT
        assert requests.get(f'{users_endpoint}/{current_id}').status_code == HTTPStatus.NOT_FOUND

    def test_delete_not_exist_user(self, users_endpoint):
        user_id = 1000

        delete_response = requests.delete(f"{users_endpoint}/{user_id}")
        assert delete_response.status_code == HTTPStatus.NOT_FOUND
