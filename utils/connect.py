# -*- coding:utf8 -*-
import socket
import time
from multiprocessing.dummy import Pool as ThreadPool

from common import adapt_encoding

def get_connect_time(ipaddress):
    HTTPS_PORT = 443
    port = HTTPS_PORT   # use HTTPS default port to connect
    timeout = 1         # set availability time to 1 sec
    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket()
        start = time.time()
        s.connect((ipaddress, port))
        end = time.time()
    except:
        msg = adapt_encoding('%s 连接超时' %(ipaddress))
        return (None,ipaddress,msg)
    else:  
        connect_time = int((end-start)*1000) # convert time to milliseconds
        msg = adapt_encoding('%s 连接时间:%s ms' %(ipaddress,connect_time))
        return (connect_time,ipaddress,msg)
    finally:
        s.close()

def get_useful_ip(iplist,thread_number):
    usefulip = []
    pool = ThreadPool(thread_number)
    while iplist:
        ip_list = iplist[:min(len(iplist),thread_number)]
        results = pool.map(get_connect_time,ip_list)
        for delay,ip,msg in results:
            print(msg)
            if delay:
                usefulip.append((delay,ip))
        iplist = iplist[thread_number:]
    usefulip.sort()     # sort reachable ips by the order of delay
    return [ip for delay,ip in usefulip]    # return just the ip list

def filter_useful_ip(iplist,thread_number=16):
    print(adapt_encoding('从%s个候选IP中进行筛选'%(len(iplist))))
    print(adapt_encoding('开始连接测试...'))
    print('-'*30)
    
    usefulip = get_useful_ip(iplist,thread_number)
    print(adapt_encoding("共找到%s个可用的ip地址")%(len(usefulip)))
    print(usefulip)
    return usefulip