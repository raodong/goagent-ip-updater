# -*- coding:utf8 -*-
import platform

def adapt_encoding(msg):
    os_type = platform.platform().lower()
    if os_type.startswith("windows"):
        return msg.decode("utf8").encode("gbk")
    else:
        return msg