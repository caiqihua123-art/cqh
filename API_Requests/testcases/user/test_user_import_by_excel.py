from API_Requests.utils.assert_utils import assert_http_business
from API_Requests.business.user_api import User
from API_Requests.utils.yaml_utils import excel_path, update_support

def test_import_user_by_excel(api, auto_log):
    """
    导入excel用户
    """

    user = User(api)
    response = user.import_excel(file_path=excel_path, update_support=update_support)
    data = assert_http_business(response, auto_log)

    msg = data.get("msg", "")
    assert "共 1 条" in msg, f"导入的条数不正确:{msg!r}"
    assert "test_excel" in msg, f"导入的账号不正确:{msg!r}"

    auto_log.info("excel文件上传+导入成功")

