import requests
import os

# 登录请求
def login(loginUrl,code,password,token,verCode):
    headers = {
        'Connection': 'Keep-Alive',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        "Content-Type": "application/json;charset=UTF-8"
    }
    data ={
    "Code": code,
    "Password": password,
    "Token": token,
    "VerCode": verCode,
    "WechatUserinfoCode": None
    }
    response = requests.post(
                            url = loginUrl,
                            json = data,
                            headers = headers,
                            allow_redirects=False)
    cookie = ""
    if(response.json()['code'] == 0):  # 登陆成功
        for ck in response.cookies:
            cookie += ck.name + "=" + ck.value + "; "
        cookie = cookie[:-2]

    return response.json(),cookie

if __name__ == '__main__':
    pass