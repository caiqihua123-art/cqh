import os
import yaml

def get_yaml_data(file_path):
    # 先获取当前绝对路径
    current_file_path = os.path.abspath(__file__)

    # 再到上一级的当前目录unitils
    curr_dir = os.path.dirname(current_file_path)

    # 再到根目录API_requests
    project_root = os.path.dirname(curr_dir)

    # 最后拼接路径
    full_file_path = os.path.join(project_root, file_path)

    # 读取YAML文件
    with open(full_file_path, 'r', encoding="UTF-8") as f:
        return yaml.safe_load(f)

# 用户表测试数据
try:
    user_data = get_yaml_data("data/user_data.yaml")
except FileNotFoundError:
    raise FileNotFoundError("data/user_data.yaml 文件不存在,请检查路径")
except yaml.YAMLError as e:
    raise yaml.YAMLError(f"文件格式不是yaml:{e}")

user_search_by_name = user_data["user_search_by_name"]
user_search_by_phonenumber = user_data["user_search_by_phonenumber"]
user_search_by_status_normal = user_data["user_search_by_status_normal"]
user_search_by_status_disabled = user_data["user_search_by_status_disabled"]
user_search_by_create_time_normal = user_data["user_search_by_create_time_normal"]
user_search_by_create_time_disabled = user_data["user_search_by_create_time_disabled"]

# 新增用户
user_info = user_data["user_add_search_edit_delete"]

# 改变用户状态
user_status = user_data["user_edit_status"]

# 重置密码
user_reset_password = user_data["user_reset_password"]

# 批量删除用户
ids = user_data["user_batch_delete"]["batch_user_ids"]

# excle导入用户
excel_path = user_data["import_user_by_excel"]["file_path"]
update_support = user_data["import_user_by_excel"]["update_support"]

# 用户中心上传图片
picture_path = user_data["user_avatar_upload"]["file_path"]


# 部门 表测试数据
try:
    dept_data = get_yaml_data("data/dept_data.yaml")
except FileNotFoundError:
    raise FileNotFoundError("data/dept_data.yaml 文件不存在,请检查文件路径")
except yaml.YAMLError as e:
    raise yaml.YAMLError(f"data/dept_data.yaml 文件格式错误:{e}")

# 部门名称
deptName = dept_data['dept_search_by_name']
# 部门状态
deptStatus = dept_data['dept_search_by_status']
# 新增部门数据
deptInfo = dept_data['deptInfo']
# 删除部门
dept_id = dept_data['dept_delete']['dept_id']

if __name__ == "__main__":
    user_data = get_yaml_data("data/dept_data.yaml")
    print(dept_id)


