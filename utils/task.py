# -*- coding:utf8 -*-
import os
from common import get_system_type,adapt_encoding

def kill_legacy_process(os_type):
    if os_type == "Windows":
        import subprocess
        proc_list = subprocess.check_output("tasklist")
        if "goagent.exe" in proc_list:
            subprocess.call("taskkill /F /IM goagent.exe /T")
    elif os_type == "Linux":
        pass

def start_goagent(os_type,goagent_path):
    kill_legacy_process(os_type)
    if os_type == "Windows":
        import os
        os.startfile(goagent_path)
    elif os_type == "Linux":
        pass

def auto_start(goagent_path):
    if os.path.exists(goagent_path):
        os_type = get_system_type()
        start_goagent(os_type,goagent_path)
        print(adapt_encoding("goagent已成功启动"))
    else:
        print(adapt_encoding("无法找到goagent启动文件，请手动开启"))