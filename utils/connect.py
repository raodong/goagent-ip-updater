# -*- coding:utf8 -*-
import socket
import time
from multiprocessing.dummy import Pool as ThreadPool

from common import adapt_encoding
from domain import verify_server

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
        return (None,ipaddress)
    else:  
        connect_time = int((end-start)*1000) # convert time to milliseconds
        return (connect_time,ipaddress)
    finally:
        s.close()

def get_useful_ip(iplist,thread_number):
    usefulip = []
    pool = ThreadPool(thread_number)
    scanned = 0
    while iplist and len(usefulip)<20:
        ipbatch = iplist[:min(len(iplist),thread_number)]
        results = pool.map(get_connect_time,ipbatch)
        reachables = [ip for delay,ip in results if delay]
        results = pool.map(verify_server,reachables)
        valid_ip = [ip for valid,ip in results if valid]
        usefulip.extend(valid_ip)
        if len(usefulip)>=20:
            break
        iplist = iplist[thread_number:]
        scanned += len(ipbatch)
        print(adapt_encoding("可用IP数/已扫描IP数：%s/%s"%(
            len(usefulip),scanned)))
    return usefulip    # return just the ip list

def filter_useful_ip(iplist,thread_number=16):
    print(adapt_encoding('从%s个候选IP中进行筛选'%(len(iplist))))
    print(adapt_encoding('%s个线程同时开始连接测试...'%(thread_number)))
    print('-'*30)
    
    usefulip = get_useful_ip(iplist,thread_number)
    print(adapt_encoding("共找到%s个可用的ip地址")%(len(usefulip)))
    print(usefulip)
    return usefulip