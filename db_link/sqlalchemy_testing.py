# mysql orm框架

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
import time

# 创建连接引擎
'''
MySQL-Python
    mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>
  
pymysql
    mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
  
MySQL-Connector
    mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
  
cx_Oracle
    oracle+cx_oracle://user:pass@host:port/dbname[?key=value&key=value...]
'''
engine = sqlalchemy.create_engine("mysql+pymysql://root:123456@23.234.53.46:3306/test")

base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


def total_time(func):
    def inner():
        start_time = int(round(time.time() * 1000))
        func()
        end_time = int(round(time.time() * 1000))
        total_time = end_time - start_time
        print("finish...total time: %d ms" % total_time)

    return inner


# 创建单表对象
class UserInfo(base):
    __tablename__ = 'userinfo'
    id = Column(Integer, primary_key=True)
    username = Column(String(10))
    passwd = Column(String(10))

    def __str__(self):
        return str(self.id)+","+self.username+","+self.passwd


# 插入一条
def insert(obj):
    start_time = int(round(time.time() * 1000))
    print("正插入到db..")
    session.add(obj)
    session.commit()
    end_time = int(round(time.time() * 1000))
    total_time = end_time - start_time
    print("finish...total time: %d" % total_time)


userinfo1 = UserInfo(username="aaaa", passwd="123")


# 批量插入
@total_time
def branch_insert():
    userinfos = []
    for i in range(100):
        userinfo = UserInfo(username="user" + str(i), passwd="pwd" + str(i))
        userinfos.append(userinfo)
    session.add_all(userinfos)
    session.commit()

#查询
@total_time
def select():
    #list = session.query(UserInfo).filter(UserInfo.id.between(5, 600)).all()
    list = session.query(UserInfo).all()

    for userinfo in list:
        print(userinfo)


# insert(userinfo1)
#branch_insert()
select()