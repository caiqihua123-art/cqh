from API_Requests.business.dept_api import Dept
from API_Requests.utils.assert_utils import assert_http_business
from API_Requests.utils.faker_utils import get_dept_fake


def test_dept_update(api, auto_log, get_mysql_conn):
    """
    修改部门信息
    """
    # 先查询拿到要修改的
    dept = Dept(api)
    response = dept.search_name()
    dept_list = response.json().get("data")
    # 拿到要修改的部门表模板和id
    target_dept = [dic for dic in dept_list if dic.get("deptName") == "研发部门"][1]
    fake_dept_data = get_dept_fake()
    target_dept_id = target_dept.get("deptId")

    # 再修改部门信息
    target_dept.update(fake_dept_data)
    response = dept.update(json=target_dept)
    assert_http_business(response, auto_log)

    # 再数据库断言
    leader = target_dept.get("leader")
    phone = target_dept.get("phone")

    conn, cursor = get_mysql_conn
    sql = "select * from sys_dept where dept_id = %s"
    cursor.execute(sql, (target_dept_id,))
    result = cursor.fetchone()
    assert result[5] == leader
    assert result[6] == phone

    auto_log.info(f"部门修改后,数据库查询成功")