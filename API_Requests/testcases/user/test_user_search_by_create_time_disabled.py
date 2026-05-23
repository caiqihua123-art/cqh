from API_Requests.business.user_api import User
from API_Requests.utils.assert_utils import assert_http_business
from API_Requests.utils.yaml_utils import user_search_by_create_time_disabled


def test_user_search_by_create_time_disabled(api,auto_log):
    """
    测试用户管理的按创建时间查询（正常）
    """
    user = User(api)
    params = user_search_by_create_time_disabled

    response = user.search(params=params)
    data = assert_http_business(response,auto_log)

    assert data.get("rows") == []
    assert data.get("total") == 0
    auto_log.info("按创建时间(不存在)查询用例执行通过")