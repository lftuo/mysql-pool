#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017-10-17 13:25:51
# @File : Config.py
# @Software : PyCharm
# MySQL 配置文件
'''
dbapi ：数据库接口
mincached ：启动时开启的空连接数量
maxcached ：连接池最大可用连接数量
maxshared ：连接池最大可共享连接数量
maxconnections ：最大允许连接数量
blocking ：达到最大数量时是否阻塞
maxusage ：单个连接最大复用次数
'''
DBHOST = "localhost"
DBPORT = 3306
DBUSER = "root"
DBPWD = "123456"
DBNAME = "spider"
DBCHAR = "utf8"