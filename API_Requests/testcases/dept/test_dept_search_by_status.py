from API_Requests.business.dept_api import Dept
from API_Requests.utils.assert_utils import assert_http_business
from API_Requests.utils.yaml_utils import deptStatus


def test_dept_search_by_status(api, auto_log):
    """
    状态查询部门列表  部门状态 0:正常  1:停用
    """

    dept = Dept(api)
    params = deptStatus
    response = dept.search_status(params)
    assert_http_business(response, auto_log)

    res = response.json()
    data = res.get("data")
    for dic in data:
        assert dic.get("status") == "1"

    auto_log.info(f"按部门状态查询成功:{deptStatus}")