import math
from http import HTTPStatus

import pytest
import requests


@pytest.fixture(scope='module')
def current_count_users(users_endpoint):
    response = requests.get(users_endpoint)
    assert response.status_code == HTTPStatus.OK
    body = response.json()
    return body['total']


@pytest.mark.parametrize('size', (1, 6, 12, 100))
def test_count_users_on_page_by_size_change(users_endpoint, current_count_users, size):
    """Проверить количество пользователей на странице, при разном параметре size"""
    response = requests.get(f'{users_endpoint}', params={'page': 1, 'size': size})
    assert response.status_code == HTTPStatus.OK
    body = response.json()
    items = body['items']
    if size > current_count_users:
        size = current_count_users
    assert len(items) == size


@pytest.mark.parametrize('size', (1, 6, 12, 100))
def test_count_page_by_size_change(users_endpoint, current_count_users, size):
    """Проверить количество страниц, при разном параметре size"""
    response = requests.get(f'{users_endpoint}', params={'size': size})
    assert response.status_code == HTTPStatus.OK
    body = response.json()
    actual_pages = body['pages']
    expected_pages = math.ceil(current_count_users / size)

    assert actual_pages == expected_pages


def test_count_users_on_page_by_size_const(users_endpoint, current_count_users):
    """Проверить количество пользователей на каждой полной странице при фиксированном size"""
    size = 2
    expected_count_full_pages = math.floor(current_count_users / 2)

    for i in range(1, expected_count_full_pages):
        response = requests.get(f'{users_endpoint}', params={'page': i, 'size': size})
        assert response.status_code == HTTPStatus.OK
        body = response.json()
        assert body['page'] == i
        assert len(body['items']) == 2


def test_results_items_by_page_change(users_endpoint):
    """Проверить, что возвращаются разные данные при разных значениях page"""
    response_one = requests.get(users_endpoint, params={'page': 1, 'size': 4})
    assert response_one.status_code == HTTPStatus.OK
    body_one = response_one.json()
    response_two = requests.get(users_endpoint, params={'page': 2, 'size': 4})
    assert response_two.status_code == HTTPStatus.OK
    body_two = response_two.json()

    assert body_one['items'] != body_two['items']
    assert body_one['page'] != body_two['page']
