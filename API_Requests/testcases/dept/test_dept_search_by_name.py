from API_Requests.business.dept_api import Dept
from API_Requests.utils.assert_utils import assert_http_business
from API_Requests.utils.yaml_utils import deptName


def test_dept_search_by_name(api, auto_log):
    """
    名称查询部门
    """
    dept = Dept(api)
    params = deptName
    response = dept.search_name(params=params)
    assert_http_business(response, auto_log)

    res = response.json()
    assert res.get("data")[0].get("deptName") == deptName["deptName"]

    auto_log.info(f"按部门名称查询成功:{deptName}")

