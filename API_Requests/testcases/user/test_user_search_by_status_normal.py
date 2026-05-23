from API_Requests.business.user_api import User
from API_Requests.utils.assert_utils import assert_http_business
from API_Requests.utils.yaml_utils import user_search_by_status_normal


def test_user_search_by_status_normal(api, auto_log):
    """
    测试用户管理的按账号状态查询（正常）
    """
    user = User(api)
    params = user_search_by_status_normal

    response = user.search(params = params)
    data = assert_http_business(response, auto_log)

    assert data['total'] > 0
    for user in data['rows']:
        assert user.get('status') == "0"

    auto_log.info("按账号状态(正常)查询用例执行通过")