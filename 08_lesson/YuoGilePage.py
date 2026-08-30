import requests
import json
from dotenv import load_dotenv


class YuoGileApi:
    # Инициализация
    def __init__(self, url="https://ru.yougile.com/api-v2") -> None:

        self.url = url
        load_dotenv()

    # Создание проекта
    def create_project(self, user_id, my_key, title):
        url = f"{self.url}/projects"

        token = f"Bearer {my_key}"

        payload = json.dumps({"title": title, "users": {user_id: "admin"}})
        headers = {'Content-Type': 'application/json', 'Authorization': token}

        response = requests.post(url, headers=headers, data=payload)

        status_code = response.status_code
        resp = response.json()

        return resp, status_code

    # Изменение наименования проекта
    def update_project(self, project_id, my_key, user_id, title):
        url = f"{self.url}/projects/{project_id}"

        token = f"Bearer {my_key}"

        payload = json.dumps({
            "title": title,
            "users": {user_id: "admin"}
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': token
        }

        response = requests.put(url, headers=headers, data=payload)
        status_code = response.status_code
        updated_project = response.json()

        return updated_project, status_code

    # Получение проекта по ID
    def get_project_id(self, project_id, my_key):
        url = f"{self.url}/projects/{project_id}"

        token = f"Bearer {my_key}"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': token
            }

        response = requests.get(url, headers=headers)
        status_code = response.status_code
        resp = response.json()

        return resp, status_code
