import pymysql
from sqlalchemy.ext.declarative import declarative_base

pymysql.install_as_MySQLdb()
BASE = declarative_base()
