import os
import sys
import pytest
import requests
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from API_Requests.business.login_api import login
from API_Requests.utils.db_utils import get_db
from API_Requests.utils.log_utils import get_log
from API_Requests.utils.ApiClient_utils import ApiClient


@pytest.fixture(scope="session")
def get_session(auto_log):
    """
    获取token夹具
    :return:
    """
    session = requests.Session()
    token = login(auto_log)
    # 逻辑风险：login() 失败时仍写入 Bearer None
    assert token, "登陆失败, 未获取到token"
    session.headers["authorization"] = f"Bearer {token}"
    yield session
    session.close()


@pytest.fixture(scope="session")
def api(get_session):
    client = ApiClient(session=get_session)
    yield client


@pytest.fixture(scope="session")
def get_mysql_conn():
    """
    数据库连接夹具
    :return:
    """
    conn,cursor = get_db()
    yield conn,cursor
    cursor.close()
    conn.close()


@pytest.fixture(scope="session")
def auto_log():
    """
    日志夹具
    :return:
    """
    logger = get_log()
    yield logger


