import db
from proxy import api
import os

if __name__ == '__main__':
    all_geo = db.get_geo()
    for geo in all_geo:
        proxy = db.check_proxy(geo['country'])
        if proxy is None:
            proxy_line = api.get_proxy(geo['country'])

            proxy_list = proxy_line.split('@')

            login = proxy_list[0].split(':')[0]
            password = proxy_list[0].split(':')[1]
            ip = proxy_list[1].split(':')[0]
            port = proxy_list[1].split(':')[1]

            db.add_proxy(ip,port,'~',login,password,geo['country'])
        else:
            db.add_count_proxy(geo['country'])
            proxy_line = f"{proxy['login']}:{proxy['password']}@{proxy['ip']}:{proxy['port']}"
        os.system(f"docker run --privileged arg_d {geo['country']} {proxy_line}")
