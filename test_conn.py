#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017-10-17 13:28:40
# @File : test_conn.py
# @Software : PyCharm
# 测试对MySQL的访问
from MySqlConn import Mysql

# 申请资源
mysql = Mysql()

sqlAll = "select * from gz_lianjia_xiaoqu_all"
result = mysql.getAll(sqlAll)
if result:
    print "get all"
    for row in result:
        print "%s\t%s\t%s\t%s\t%s" % (row["area_name"], row["price"],row["longtitude"],row["latitude"],row["detail_url"])
#sqlAll = "select * from gz_lianjia_xiaoqu_all"
#result = mysql.getMany(sqlAll, 2)
#if result:
#   print "get many"
#    for row in result:
#        print "%s\t%s" % (row["area_name"], row["price"])

#result = mysql.getOne(sqlAll)
#print "get one"
#print "%s\t%s" % (result["area_name"], result["price"])

# 释放资源
mysql.dispose()