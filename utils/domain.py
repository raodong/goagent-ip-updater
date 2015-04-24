import socket
import ssl
from common import adapt_encoding

def verify_server(ip):
    timeout = 2
    valid_name = ["google.com","www.google.com","*.google.com"]
    s = socket.socket()
    s.settimeout(timeout)
    c = ssl.wrap_socket(s, cert_reqs=ssl.CERT_REQUIRED, ca_certs='cacert.pem')
    c.settimeout(timeout)
    try:
        c.connect((ip, 443))
        cert = c.getpeercert()
    except Exception as e:
        pass
    else:
        subject = cert.get("subject",[])
        try:
            d = dict([item[0] for item in subject])
            if d.get("commonName") in valid_name:
                return (True,ip)
        except Exception as e:
            pass
    return (False,ip)

if __name__ == '__main__':
    testip = "64.233.164.136|173.194.123.1|173.194.115.201|210.242.125.34|64.233.164.101|173.194.123.97|173.194.38.195|64.233.164.81"
    for ip in testip.split("|"):
        if verify_server(ip)[0]:
            print(ip)