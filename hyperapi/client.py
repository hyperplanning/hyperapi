import geopandas as gpd
import pandas as pd
import requests
import yaml


class HyperClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def login(self, username, password):
        login_url = f"{self.base_url}/login"
        credentials = {"username": username, "password": password}
        response = self.session.post(login_url, data=credentials)

        if response.status_code == 200:
            self.session.headers.update(
                {"Authorization": f"Bearer {response.json().get('token')}"}
            )
            return True
        else:
            return False

    def get(self, endpoint) -> requests.models.Response:
        url = f"{self.base_url}/{endpoint}"
        response = self.session.get(url)
        return response

    def post(self, endpoint, data) -> requests.models.Response:
        url = f"{self.base_url}/{endpoint}"
        response = self.session.post(url, json=data)
        return response

    def delete(self, endpoint, data) -> requests.models.Response:
        url = f"{self.base_url}/{endpoint}"
        response = self.session.delete(url, json=data)
        return response
