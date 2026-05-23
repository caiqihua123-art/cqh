from API_Requests.business.user_api import User
from API_Requests.utils.assert_utils import assert_http_business
from API_Requests.utils.yaml_utils import ids


def test_user_batch_delete(api, get_mysql_conn, auto_log):
    """
    批量删除用户
    """
    user = User(api)
    response = user.batch_delete(ids)
    assert_http_business(response,auto_log)
    auto_log.info(f"删除用户成功,用户id:{ids}")

    # 数据库校验
    conn, cursor = get_mysql_conn
    sql = f"select del_flag from sys_user where user_id in (%s);"
    cursor.execute(sql, (ids,))
    del_flag = cursor.fetchone()
    result = cursor.fetchall()
    print(result)
    print(type(result))
    for del_flag in result:
        assert str(del_flag[0]) == str(2)
    auto_log.info(f"数据库校验成功,用户{ids}软删除成功,del_flag:{del_flag[0]}")



