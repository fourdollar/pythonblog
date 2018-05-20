#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/03/09 14:25
# @Author  : Feng
# @Site    : 
# @File    : test.py.py
# @Software: PyCharm

# 测试orm和models的功能
import orm
from models import User,Blog,Comment
import asyncio

loop = asyncio.get_event_loop()
async def test():
    #创建连接池,里面的host,port,user,password需要替换为自己数据库的信息
    await orm.create_pool(loop=loop,host='127.0.0.1', port=3306,user='root', password='ziqing2013',db='awesome')
    #没有设置默认值的一个都不能少
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank',id="123")
    await u.save()

#把协程丢到事件循环中执行
loop.run_until_complete(test())