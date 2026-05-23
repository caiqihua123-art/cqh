import requests
from API_Requests.utils.config_utils import base_url, timeout


class ApiClient:
    def __init__(self, session):
        self.session = session
        self.base_url = base_url
        self.timeout = int(timeout)

    def _request(self,method: str, api_path: str, params=None, data=None, json=None, files=None):
        url = self.base_url + api_path
        try:
            response = self.session.request(method=method.upper(), url=url, params=params, data=data, json=json, files=
            files, timeout=self.timeout)
            return response
        except Exception as e:
            raise RuntimeError(f"HTTP请求失败:{e}")

    def get(self, api_path: str, params=None):
        return self._request("GET", api_path=api_path, params=params)

    def post(self,api_path:str, params=None, data=None, json=None, files=None):
        return self._request("POST", api_path=api_path, params=params, data=data, json=json, files=files)

    def put(self, api_path: str, params=None, data=None, json=None):
        return self._request("PUT", api_path=api_path, params=params, data=data, json=json)

    def delete(self, api_path: str, params=None,json=None):
        return self._request("DELETE", api_path=api_path, params=params, json=json)

if __name__ == "__main__":
    session = requests.Session()
    api_client = ApiClient(session)
