# -*- coding:utf8 -*-
import platform

def adapt_encoding(msg):
    os_type = platform.system()
    if os_type == "Windows":
        return msg.decode("utf8").encode("gbk")
    else:
        return msg

def get_system_type():
    return platform.system()