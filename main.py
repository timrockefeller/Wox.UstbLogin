# -*- coding: utf-8 -*-

from wox import Wox
import http.client as client
from urllib.parse import quote
import time
import sys
import getpass

###############################
##        Edit Here          ##
default_Username = ""        ##
default_Password = ""        ##
###############################


##
def get_ip():
    conn = client.HTTPConnection('cippv6.ustb.edu.cn')
    conn.request('GET', '/get_ip.php')
    res = conn.getresponse()
    if (res.status == 200):
        ip = res.read().decode('utf-8').split("'")[1]
        return ip
    return ""
class LOGIN0(Wox):


    def query(self, query):
        results = []
        if(query):
            results.append({
                "Title": "老板上机",
                "SubTitle": "使用\"账号(空格)密码\"形式",
                "IcoPath":"Images/app.ico",
                "ContextData": "ctxData",
                "JsonRPCAction":{
                    "method":"login",
                    "parameters":query.split(" ",1),
                    "dontHideAfterAction":False
                }
            })
        results.append({
            "Title": "董事长上机",
            "SubTitle": "使用"+default_Username+"直接登录",
            "IcoPath":"Images/app.ico",
            "ContextData": "ctxData",
            "JsonRPCAction": {
                "method":"login",
                "parameters":[default_Username,default_Password],
                "dontHideAfterAction":False
            }
        })
        return results

    def context_menu(self, data):
        results = []
        results.append({
            "Title": "Context menu entry",
            "SubTitle": "Data: {}".format(data),
            "IcoPath":"Images/app.ico"
        })
        return results



    def login(self,un,pw):
        # un = un_pw[0]
        # pw = un_pw[1]
        ip = get_ip()
        en_ip = quote(ip, safe='')
        en_pwd = quote(pw, safe='')
        headers = {
            "Cookie":"myusername=%s; username=%s"%(un, un),
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
            "Connection": "keep-alive",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
        }
        body = "DDDDD=%s&upass=%s&v6ip=%s&0MKKey=123456789" % (un, en_pwd, en_ip)
        conn = client.HTTPConnection('202.204.48.66')
        conn.request('POST', '/', body, headers)
        res = conn.getresponse()


if __name__ == "__main__":
    LOGIN0()
