from API_Requests.business.dept_api import Dept
from API_Requests.utils.assert_utils import assert_http_business
from API_Requests.utils.yaml_utils import deptInfo


def test_dept_add(api, auto_log, get_mysql_conn):
    """
    新增部门,数据库查询断言
    """
    dept = Dept(api)
    json_data = deptInfo
    response = dept.add(json=json_data)
    assert_http_business(response, auto_log)

    # 数据库查询
    conn, cursor = get_mysql_conn
    sql = "select * from sys_dept where dept_name = %s and parent_id = %s"
    cursor.execute(sql, (json_data["deptName"], json_data["parentId"]))
    result = cursor.fetchall()
    assert result is not None
    assert result[0][3] == json_data["deptName"]
    assert result[0][1] == json_data["parentId"]

    auto_log.info(f"新增部门,按数据库查询成功,部门名称:{result[0][3]}")