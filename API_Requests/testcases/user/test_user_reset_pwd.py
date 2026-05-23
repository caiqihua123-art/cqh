import requests
from API_Requests.business.user_api import User
from API_Requests.utils.assert_utils import assert_http_business
from API_Requests.utils.config_utils import base_url
from API_Requests.utils.yaml_utils import user_reset_password


def test_user_reset_pwd(api, auto_log, get_mysql_conn):
    """
    用户重置密码
    """
    user = User(api)
    response = user.reset_password(payload=user_reset_password)
    assert_http_business(response, auto_log)
    auto_log.info(f"重置用户密码成功,用户:{user_reset_password['userId']},密码:{user_reset_password['password']}")

    # 数据库拿姓名
    conn, cursor = get_mysql_conn
    sql = "select user_name from sys_user where user_id = %s"
    cursor.execute(sql, (user_reset_password['userId']),)
    username = cursor.fetchone()[0]
    print(username)

    # 数据库密码存的是哈希,用登陆做校验
    url = f"{base_url}/login"
    data_json = {"username": username, "password": user_reset_password['password']}
    response = requests.post(url, json=data_json)
    assert_http_business(response, auto_log)
    auto_log.info("密码修改成功，登录校验成功")