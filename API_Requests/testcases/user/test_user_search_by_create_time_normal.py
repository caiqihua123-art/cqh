from API_Requests.business.user_api import User
from API_Requests.utils.assert_utils import assert_http_business
from API_Requests.utils.yaml_utils import user_search_by_create_time_normal



def test_user_search_by_create_time_normal(api,auto_log):
    """
    测试用户管理的按创建时间查询（不存在）
    """
    user = User(api)
    params = user_search_by_create_time_normal

    response = user.search(params=params)
    data = assert_http_business(response,auto_log)

    rows = data.get("rows")
    for user in rows:
        assert "createTime" in user
        assert user["createTime"] is not None

    auto_log.info("按创建时间(存在)查询用例执行通过")