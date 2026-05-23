import pymysql
from API_Requests.utils.config_utils import get_config


def get_db():
    config = get_config()
    conn = pymysql.connect(
        host=config['mysql']['host'],
        port=int(config['mysql']['port']),
        user=config['mysql']['user'],
        password=config['mysql']['password'],
        db=config['mysql']['db'],
        charset=config['mysql']['charset']
    )
    cursor = conn.cursor()
    return conn, cursor
