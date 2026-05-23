from API_Requests.business.user_api import User
from API_Requests.utils.assert_utils import assert_http_business
from API_Requests.utils.yaml_utils import user_search_by_phonenumber


def test_user_search_by_phone(api,auto_log):
    """
    测试用户管理的按创建按手机号查询
    """
    user = User(api)
    params = user_search_by_phonenumber
    response = user.search(params=params)
    data = assert_http_business(response,auto_log)

    # 断言到至少有一条数据
    assert data["total"] > 0
    assert len(data["rows"]) > 0
    # 断言取到的手机号
    has_target_user = False
    for user in data.get("rows"):
        if user.get("phonenumber") == "15888888888":
            has_target_user = True
    assert has_target_user
    auto_log.info("按手机号查询用例执行通过")

