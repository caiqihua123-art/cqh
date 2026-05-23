

class Dept:
    """
    封装部门增删改查操作
    """
    def __init__(self, api):
        self.api = api


    def search_name(self, params=None):
        """
        名称查询部门列表。'params' 可选，不传时查询全部。
        """
        path = "/system/dept/list"
        return self.api.get(api_path=path, params=params)


    def search_status(self, params=None):
        """
        状态查询部门列表。'params' 可选，不传时查询全部。
        """
        path = "/system/dept/list"
        return self.api.get(api_path=path, params=params)


    def add(self, json):
        """
        新增部门
        """
        path = "/system/dept"
        return self.api.post(api_path=path, json=json)


    def update(self, json):
        """
        修改部门信息
        """
        path = "/system/dept"
        return self.api.put(api_path=path, json=json)