import os
import pytest
from dotenv import load_dotenv
from YuoGilePage import YuoGileApi


load_dotenv()


# Фикстуры
@pytest.fixture
def api():
    return YuoGileApi()


@pytest.fixture
def project_id(api):
    user_id = os.getenv('USER_ID')
    my_key = os.getenv('MY_KEY')
    title = "Проект для тестов"

    resp, status_code = api.create_project(user_id, my_key, title)

    yield resp


class TestPositive:

    def test_create_project_positive(self, api):
        my_key = os.getenv('MY_KEY')
        user_id = os.getenv("USER_ID")
        title = "Проект 1"

        """Позитивный: создание проекта"""
        resp, status_code = api.create_project(user_id, my_key, title)

        assert status_code == 201
        assert resp["id"] is not None

    def test_update_project_positive(self, api, project_id):
        my_key = os.getenv('MY_KEY')
        user_id = os.getenv("USER_ID")
        new_title = "Обновленное наименование"

        """Позитивный: обновление проекта"""
        updated_project, status_code = api.update_project(
            project_id['id'], my_key, user_id, new_title)

        assert status_code == 200
        assert updated_project is not None

    def test_get_project_positive(self, api: YuoGileApi, project_id):
        """Позитивный: получение проекта по ID"""
        my_key = os.getenv('MY_KEY')

        resp, status_code = api.get_project_id(project_id['id'], my_key)

        assert status_code == 200
        assert resp['id'] == project_id['id']


class TestNegative:
    def test_create_project_negative(self, api):
        my_key = os.getenv('MY_KEY')
        user_id = os.getenv('MISS_USER_ID')
        title = "Проект 1"

        """Негативный: создание проекта"""
        resp, status_code = api.create_project(user_id, my_key, title)
        assert status_code == 400
        assert (resp['message'] ==
                'Сотрудники со следующими ID не найдены в компании:'
                ' jffdhugyugbu')
        assert resp['error'] == 'Bad Request'

    def test_create_project_negative1(self, api):
        my_key = os.getenv('MY_KEY')
        user_id = os.getenv('USER_ID')
        title = ""

        """Негативный: создание проекта без наименования"""
        resp, status_code = api.create_project(user_id, my_key, title)

        assert status_code == 400
        assert (resp['message'] ==
                ['title should not be empty'])
        assert resp['error'] == 'Bad Request'

    def test_update_project_negative(self, api, project_id):
        my_key = os.getenv('MY_KEY')
        user_id = os.getenv("USER_ID")
        new_title = "Обновленное наименование"

        """Негативный: обновление проекта"""
        updated_project, status_code = api.update_project(
            '4a21-9cb5-6a936bda7397', my_key, user_id, new_title)

        assert status_code == 404
        assert "Проект не найден" in updated_project.get("message")

    def test_get_project_negative(self, api: YuoGileApi, project_id):

        my_key = os.getenv('MY_KEY')
        """Негативный: получение проекта по ID"""
        resp, status_code = api.get_project_id(
            '4a21-9cb5-6a936bda7397', my_key)

        assert status_code == 404
        assert "Проект не найден" in resp.get("message")
