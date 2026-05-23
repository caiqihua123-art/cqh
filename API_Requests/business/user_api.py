import os
from API_Requests.utils.excel_utils import ExcelHandler


class User:
    """
    封装用户的增删改查等操作
    """

    def __init__(self, api):
        self.api = api


    def search(self, params=None):
        """
        查询用户列表。'params' 可选，不传时查询全部。
        """
        path = "/system/user/list"
        return self.api.get(api_path=path, params=params)


    def add(self, payload):
        """
        新增用户。
        """
        path = "/system/user"
        return self.api.post(api_path=path, json=payload)


    def edit(self, payload):
        """
        修改用户。
        """
        path = "/system/user"
        return self.api.put(api_path=path, json=payload)


    def delete(self, user_id):
        """
        删除用户。
        """
        path = f"/system/user/{user_id}"
        return self.api.delete(api_path=path)


    def batch_delete(self, ids):
        """
        批量删除用户
        """
        path = f"/system/user/{ids}"
        return self.api.delete(api_path=path)


    def change_status(self, payload):
        """
        改变用户状态：1 为停用，0 为正常。
        """
        path = "/system/user/changeStatus"
        return self.api.put(api_path=path, json=payload)


    def reset_password(self, payload):
        """
        重置用户密码。
        """
        path = "/system/user/resetPwd"
        return self.api.put(api_path=path, json=payload)


    def upload_avatar(self, file_path):
        """
        上传用户头像。
        """
        path = "/system/user/profile/avatar"
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"文件不存在: {file_path}")

        with open(file_path, "rb") as f:
            files = {"avatarfile": f}
            return self.api.post(api_path=path, files=files)


    def export_excel(self, file_path):
        """
        导出用户 Excel。
        :param file_path: 规定excel导出后的位置和名称
        :return:不含第一行标题的excel内容
        """
        path = "/system/user/export"
        response = self.api.post(api_path=path)
        if response is None:
            raise ConnectionError("导出请求未收到响应")

        # 检查Content_Type
        content_type = response.headers.get("Content-Type", "")
        if "spreadsheet" not in content_type.lower() and "octet-stream" not in content_type.lower():
            raise RuntimeError(f"导出来的格式不是Excel格式, content-type: {content_type!r}")

        with open(file_path, "wb") as f:
            f.write(response.content)

        excel = ExcelHandler(file_path)
        return excel.read_excel()


    def import_excel(self, file_path: str, update_support: bool = True):
        """
        导入用户 Excel。
        :param file_path: 导入的 Excel 路径
        :param update_support: 是否覆盖，True=覆盖，False=不覆盖
        :return: 接口响应对象；文件不存在时返回 None
        """
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"导入文件不存在: {file_path}")

        path = f"/system/user/importData?updateSupport={str(update_support).lower()}"
        with open(file_path, "rb") as f:
            files = {"file": f}
            return self.api.post(api_path=path, files=files)



