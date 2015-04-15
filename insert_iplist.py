# -*- coding:utf8 -*-

def get_iplist(ip_file):
    with open(ip_file,"rb") as f:
        lines = iter(f)
        return next(lines)

def read_file(ini_file,iplist):
    ini_content = []
    with open(ini_file,"rb") as f:
        for line in f:
            if line.startswith("google_cn"):
                line = "google_cn = %s\r\n"%(iplist)
            elif line.startswith("google_hk"):
                line = "google_hk = %s\r\n"%(iplist)
            elif line.startswith("google_talk"):
                line = "google_talk = %s\r\n"%(iplist)
            ini_content.append(line)
        return ini_content

def write_file(ini_file,ini_content):
    with open(ini_file,"wb") as f:
        for line in ini_content:
            f.write(line)

def update_ini():
    ip_file = "output.txt"
    ini_file = "local/proxy.ini"
    iplist = get_iplist(ip_file)
    new_content = read_file(ini_file,iplist)
    write_file(ini_file,new_content)

if __name__ == '__main__':
    update_ini()