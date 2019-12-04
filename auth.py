import requests
import execjs
import os

inf = open("./userinfo.ini","r",encoding = 'UTF-8')
userstr = ''
userstr = userstr + inf.readline()
user = eval('{'+userstr+'}')

outdata = {
    "action": "login",
    "username": user['username'],
    "password": user['password'],
    "ac_id": "1",
    "ip": "",
}

def getLOG_JS():
    JSf = open("./log.js",'r',encoding = 'UTF-8')
    line = JSf.readline()
    Jstr = ''
    while line:
        Jstr = Jstr+line
        line = JSf.readline()
    return Jstr
logJS = getLOG_JS()
logOP = execjs.compile(logJS)


def auth(challenge,srun):
    param_challenge = {
        "callback":"jQuery",
        "username":user['username'],
        "ip":"",
        "double_stack":"1",
        }

    r = requests.get(challenge,params=param_challenge)
    strofr = str(r.content,encoding = 'UTF-8')
    strofr = strofr[7:-1]
    rdata = eval(strofr)

    result = logOP.call('getOutData',outdata,rdata)
    param_srun = {
        "callback":"jQuery",
        "action":"login",
        "username":user['username'],
        "password":result['password'],
        "ac_id":"1",
        "info":result['info'],
        "chksum":result['chksum'],
        "n":"200",
        "type":"1",
    }

    r2 = requests.get(srun,params=param_srun)
    msg = eval(r2.content[7:-1])
    return msg["error_msg"]
try:
    ipv4_challenge = "https://auth4.tsinghua.edu.cn/cgi-bin/get_challenge"
    ipv4_srun = "https://auth4.tsinghua.edu.cn/cgi-bin/srun_portal"
    ipv4 = auth(ipv4_challenge,ipv4_srun)
    if ipv4=="":
        print("ipv4 login successful")
        flag4 = True
    else:
        print("ipv4 login failed, error " + ipv4)
        flag4 = False
except:
    flag4 = False

try:
    ipv6_challenge = "https://auth6.tsinghua.edu.cn/cgi-bin/get_challenge"
    ipv6_srun = "https://auth6.tsinghua.edu.cn/cgi-bin/srun_portal"
    ipv6 = auth(ipv6_challenge,ipv6_srun)
    if ipv6=="":
        print("ipv6 login successful")
        flag6 = True
    else:
        print("ipv6 login failed, error " + ipv6)
        flag6 = False
except:
    flag6 = False


os.system('pause')