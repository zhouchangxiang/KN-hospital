import configparser
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(BASE_DIR, r'database\config.ini')
# CONFIG_DIR = "D:\\KN-hospital\\database\\config.ini"
config = configparser.ConfigParser()
config.read(CONFIG_DIR, encoding='UTF-8')

REDIS_HOST = config['data_realtime_server']['host']
REDIS_TABLENAME = config['data_realtime_server']['tablename']
# REDIS_ZENGLIANG = config['data_realtime_server']['db_zengliang']
REDIS_PORT = int(config['data_realtime_server']['port']) if config['data_realtime_server'][
    'port'].isdigit() else 6379
REDIS_PASSWORD = config['data_realtime_server']['password']

MES_DATABASE_HOST = config['MES_DataBase']['host']
MES_DATABASE_USER = config['MES_DataBase']['user']
MES_DATABASE_PASSWD = config['MES_DataBase']['password']
MES_DATABASE_NAME = config['MES_DataBase']['database']
MES_DATABASE_CHARSET = config['MES_DataBase']['charset']

DB_URL = 'mysql+pymysql://root:1qaz2wsx@127.0.0.1:3306/hstl?charset=utf8&autocommit=true'
