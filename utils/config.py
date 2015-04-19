# -*- coding:utf8 -*-
from common import adapt_encoding

def config_thread_num():
    num = raw_input(adapt_encoding("请设置同时测试的连接数，默认为16："))
    while True:
        if not num:
            return 16
        try:
            num = int(num)
        except ValueError:
            num = raw_input(adapt_encoding("输入有误，请输入正确格式的数字："))
        else:
        	if num<0:
        		num = raw_input(adapt_encoding("并发连接数至少为1，请重新输入："))
        	elif num>64:
        		num = raw_input(adapt_encoding("并发连接数最大为64，请重新输入："))
        	else:
        		return num