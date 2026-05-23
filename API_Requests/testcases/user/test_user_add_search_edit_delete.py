from API_Requests.utils.assert_utils import assert_http_business
from API_Requests.utils.config_utils import base_url
from API_Requests.utils.yaml_utils import user_info
from API_Requests.utils.faker_utils import get_user_fake


def test_user_add_search_edit_delete(get_session, auto_log, get_mysql_conn):
    """
    用户：新增 -> 查询 -> 编辑 -> 删除 流程测试
    """
    # ======================

    # 1. 假数据新增用户
    # ======================
    url = f"{base_url}/system/user"

    # 组装请求参数：yaml模板 + faker假数据
    json_data = user_info
    faker_data = get_user_fake()
    json_data.update(faker_data)

    # 发送新增请求
    response = get_session.post(url, json=json_data)

    # 公共断言
    data = assert_http_business(response, auto_log)
    auto_log.info("发送请求-新增用户成功")

    # ======================
    # 2. 数据库查询新增用户
    # ======================
    # 拿新增用户姓名
    user_name = faker_data["userName"]

    # 查询sql
    conn, cursor = get_mysql_conn
    sql = f"select * from sys_user where user_name = %s"
    cursor.execute(sql, (user_name,))
    result = cursor.fetchone()

    # 断言数据库
    assert result is not None
    auto_log.info(f"查询数据库-新增成功,user_name:{user_name}")

    # 从数据库查询的元组取出数据
    user_id = result[0]
    real_user_name = result[2]

    # ======================
    # 3. 接口查询新增用户
    # ======================
    search_url = f"{base_url}/system/user/list"
    params = {"userName": real_user_name}
    # 发送查询请求
    response = get_session.get(search_url, params=params)

    # 断言公共业务
    data = assert_http_business(response, auto_log)

    # 业务断言
    assert data is not None
    assert data.get("total") == 1
    assert data.get("rows")[0]["userName"] == real_user_name
    assert data.get("rows")[0]["userId"] == user_id
    auto_log.info(f"发送请求查询-新增用户成功,user_name:{real_user_name}, user_id:{user_id}")

    # ======================
    # 4. 接口修改用户
    # ======================
    edit_url = f"{base_url}/system/user/"
    edit_faker_data = get_user_fake()
    edit_faker_data["userId"] = user_id
    edit_json_data = {}
    edit_json_data.update(edit_faker_data)

    # 发送修改请求
    response = get_session.put(edit_url, json=edit_json_data)
    # 断言公共业务
    data = assert_http_business(response, auto_log)
    auto_log.info("发送请求,修改用户成功")

    # ======================
    # 5. 数据库查询是否修改成功
    # ======================

    # 一定要加这句刷新数据库缓存,上面已经用过数据库查询了，还在旧的
    conn.commit()
    edit_user_name = edit_json_data["userName"]
    sql = f"select * from sys_user where user_name = %s"
    cursor.execute(sql, (edit_user_name,))
    result = cursor.fetchone()
    # 断言修改后数据库
    assert result is not None
    assert result[2] == edit_user_name
    auto_log.info(f"查询修改后数据库成功,user_name:{edit_user_name}, user_id:{user_id}")

    # ======================
    # 6. 发送请求删除用户
    # ======================
    delete_url = f"{base_url}/system/user/{user_id}"
    response = get_session.delete(delete_url)
    data = assert_http_business(response, auto_log)
    auto_log.info("发送请求删除成功")

    # ======================
    # 7. 数据库查询删除，并真正删除
    # ======================
    # 先数据库查询
    conn.commit()
    sql = f"select * from sys_user where user_id = %s"
    cursor.execute(sql, (user_id,))
    result = cursor.fetchone()
    assert result is not None
    assert result[11] == '2'
    auto_log.info(f"软删除校验成功,del_flag = 2")

    # 数据库删除
    sql = f"delete from sys_user where user_id = %s"
    cursor.execute(sql, (user_id,))
    conn.commit()

    # 删除之后再查询
    sql = f"select * from sys_user where user_id = %s"
    cursor.execute(sql, (user_id,))
    result = cursor.fetchone()
    assert result is None
    auto_log.info("数据库删除成功")


