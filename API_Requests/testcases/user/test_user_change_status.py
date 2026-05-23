from API_Requests.business.user_api import User
from API_Requests.utils.assert_utils import assert_http_business
from API_Requests.utils.yaml_utils import user_status


def test_user_change_status(api, auto_log, get_mysql_conn):
    """
    改变用户状态 1 : 停用  0 : 正常
    """

    # 发送请求修改用户状态
    user = User(api)
    json_data = user_status
    response = user.change_status(payload=json_data)
    data = assert_http_business(response, auto_log)
    auto_log.info(f"用户改变状态成功,user_id:{json_data['userId']}, status:{json_data['status']}")

    # 数据库校验
    conn,cursor = get_mysql_conn
    use_id = json_data['userId']
    sql = f"select * from sys_user where user_id = %s"
    cursor.execute(sql, (use_id,))
    result = cursor.fetchone()

    # 防止数据为空去下标报错
    assert result is not None, f"数据库未查询到 userid = {use_id} 的数据"
    assert str(result[10]) == str(json_data['status'])
    auto_log.info(f"数据库校验成功,user_id:{json_data['userId']},status:{json_data['status']}")





