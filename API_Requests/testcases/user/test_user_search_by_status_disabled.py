from API_Requests.business.user_api import User
from API_Requests.utils.assert_utils import assert_http_business
from API_Requests.utils.yaml_utils import user_search_by_status_disabled


def test_user_search_by_status_disabled(api,auto_log):
    """
    测试用户管理的按账号状态查询（停用）
    """
    user = User(api)
    params = user_search_by_status_disabled

    response = user.search(params=params)
    data = assert_http_business(response,auto_log)

    for user in data.get("rows"):
        assert user.get("status") == "1"

    auto_log.info("按账号状态(停用)查询用例执行通过")