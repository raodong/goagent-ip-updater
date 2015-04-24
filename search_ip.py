# -*- coding:utf8 -*-
from utils.config import config_thread_num
from utils.common import adapt_encoding
from utils.connect import filter_useful_ip
from utils.io import get_iplist,update_ini
from utils.task import auto_start

def main():
    try:
        with open("cacert.pem","rb") as f:
            pass
    except IOError:
        print(adapt_encoding("未找到证书文件，请将cacert.pem放在同一目录下"))
        raw_input(adapt_encoding("输入回车退出..."))
        return None
    try:
        thread_num = config_thread_num()
        ip_file = "iplist.txt"
        iplist = get_iplist(ip_file)
        useful_ip = filter_useful_ip(iplist,thread_num)
    except Exception as e:
        print(e)
    else:
        if not useful_ip:
            print(adapt_encoding("未找到可用IP地址，请更新IP源"))
        else:
            try:
                ini_file = "local/proxy.ini"
                update_ini(useful_ip,ini_file)
            except IOError as e:
                ip_file = "iplist.txt"
                with open(ip_file, 'wb') as f:
                    text='|'.join(useful_ip)
                    f.write(text)
                print(adapt_encoding("请将程序放在goagent目录下，"+
                    "与local和server文件夹并列，以自动更新goagent配置文件"))
            except Exception as e:
                print(e)
            else:
                print(adapt_encoding("配置文件更新成功"))
                goagent_path = os.path.join(
                        os.path.abspath(os.path.dirname("__file__")),
                        "local/goagent.exe")
                auto_start(goagent_path)
    raw_input(adapt_encoding("输入回车退出..."))

if __name__ == '__main__':
    main()