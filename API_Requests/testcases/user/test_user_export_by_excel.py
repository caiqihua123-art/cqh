from API_Requests.business.user_api import User

def test_export_user_by_excel(api, auto_log):
    """
    导出用户excel
    """
    user = User(api)
    result = user.export_excel(file_path=r"C:\Users\Administrator\Desktop\export.xlsx")

    assert len(result) > 0
    assert len(result[0]) == 11
    assert len(result) >= 1
    auto_log.info("导出excel文件成功,数据正确")

