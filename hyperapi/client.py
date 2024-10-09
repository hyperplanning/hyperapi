import geopandas as gpd
import pandas as pd
import requests


class HyperClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def login(self, username, password):
        login_url = f"{self.base_url}/login/access-token"
        credentials = {"username": username, "password": password}
        response = self.session.post(login_url, data=credentials)

        if response.status_code == 200:
            self.session.headers.update(
                {"Authorization": f"Bearer {response.json().get('access_token')}"}
            )
            return True
        else:
            print("Login unsuccessful!")
            return False

    def get(self, endpoint, params=None) -> requests.models.Response:
        url = f"{self.base_url}/{endpoint}"
        response = self.session.get(url, params=params)
        if response.status_code != 200:
            raise Exception(f"Call unsuccessful with status code {response.status_code}")
        return response

    def post(self, endpoint, data) -> requests.models.Response:
        url = f"{self.base_url}/{endpoint}"
        response = self.session.post(url, json=data)
        return response

    def delete(self, endpoint, data) -> requests.models.Response:
        url = f"{self.base_url}/{endpoint}"
        response = self.session.delete(url, json=data)
        return response
