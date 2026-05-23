from API_Requests.business.user_api import User
from API_Requests.utils.assert_utils import assert_http_business
from API_Requests.utils.yaml_utils import user_search_by_name


def test_user_search_by_name(api, auto_log):
    """
    测试用户管理的按创建按姓名查询
    """
    user = User(api)
    params = user_search_by_name

    response = user.search(params=params)
    data = assert_http_business(response,auto_log)

    assert data.get("total") > 0
    assert len(data.get("rows")) > 0
    assert data.get("rows")[0].get("userName") == "admin"
    assert data.get("rows")[0].get("phonenumber") == "15888888888"

    auto_log.info("按姓名查询用例执行通过")

