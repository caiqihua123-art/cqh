import os
from configparser import ConfigParser

def get_config():
    config = ConfigParser()
    # 先获取当前绝对路径
    current_file_path = os.path.abspath(__file__)

    # 再到上一级的当前目录unitils
    curr_dir = os.path.dirname(current_file_path)

    # 再到根目录API_requests
    project_root = os.path.dirname(curr_dir)

    # 最后拼接路径
    full_file_path = os.path.join(project_root, "config/config.ini")

    config.read(full_file_path)
    return config

config = get_config()
base_url = config["env"]["base_url"]
timeout = config["env"]["timeout"]

username = config["admin"]["username"]
password = config["admin"]["password"]


