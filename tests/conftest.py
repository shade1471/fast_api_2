import os

import dotenv
import pytest


@pytest.fixture(scope='session', autouse=True)
def envs():
    dotenv.load_dotenv()

@pytest.fixture(scope='session')
def app_url():
    return os.getenv("APP_URL")

@pytest.fixture(scope='session')
def users_endpoint():
    app_url = os.getenv("APP_URL")
    return f'{app_url}/api/users'