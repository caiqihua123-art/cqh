import logging
import os

def get_log():
    logger = logging.getLogger('若依自动化测试日志')
    logger.setLevel(logging.DEBUG)
    # 防止日志重复打印
    if logger.handlers:
        return logger

    # 设置格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # 控制台输出
    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)
    sh.setFormatter(formatter)

    # 文件输出
    log_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "logs/log.txt")
    # 确保存在
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    fh = logging.FileHandler(log_path, encoding="utf-8")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)

    # 绑定
    logger.addHandler(fh)
    logger.addHandler(sh)

    return logger

