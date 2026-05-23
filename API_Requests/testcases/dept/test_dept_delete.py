from API_Requests.business.dept_api import Dept
from API_Requests.utils.assert_utils import assert_http_business
from API_Requests.utils.yaml_utils import dept_id


def test_dept_delete(api, auto_log, get_mysql_conn):
    """
    删除部门
    """
    dept = Dept(api)
    response = dept.delete(dept_id=dept_id)
    assert_http_business(response, auto_log)

    # 数据库查询,软删除del_flag=2
    conn, cursor = get_mysql_conn
    sql = "SELECT * FROM sys_dept WHERE dept_id = %s"
    cursor.execute(sql, (dept_id,))
    result = cursor.fetchone()
    assert str(result[9]) == "2"

    auto_log.info(f"删除部门,按数据库查询删除成功")

