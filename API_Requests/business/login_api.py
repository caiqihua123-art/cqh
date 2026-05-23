import requests
from API_Requests.utils.assert_utils import assert_http_business
from API_Requests.utils.config_utils import base_url, username, password


def login(auto_log):
    """
    封装登录方法
    :return:
    """
    url = f"{base_url}/login"
    data_json = {"username": username, "password": password}
    response = requests.post(url, json=data_json)
    res = assert_http_business(response, auto_log)

    token = res.get("token")
    if not token:
        raise ValueError(f"接口未返回token")
    return token




