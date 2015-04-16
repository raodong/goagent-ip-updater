# -*- coding:utf8 -*-
from common import adapt_encoding

def config_thread_num():
    print(adapt_encoding("请设置同时测试的连接数，默认为16："))
    while True:
        num = raw_input()
        if not num:
            return 16
        try:
            return int(num)
        except ValueError:
            print(adapt_encoding("输入有误，请输入正确格式的数字："))
