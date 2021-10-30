import requests
import os

# 登录请求
def commit(commitUrl,RealAddress,RealCity,RealCounty,RealProvince,BackState,MorningTemp,NightTemp,cookie):
    headers = {
        'Connection': 'keep-alive',
        'Content-Length': '527',
        'Content-Type': 'application/json;charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
        "Cookie":"Hm_lvt_d7e34467518a35dd690511f2596a570e=1613005032,1613005965,1613011499,1613071563; Hm_lpvt_d7e34467518a35dd690511f2596a570e=1613071563; "+cookie,
    }
    data ={
        "BackState": BackState,
        "Latitude": None,
        "Longitude": None,
        "MorningTemp": MorningTemp,
        "NightTemp": NightTemp,
        "RealAddress": RealAddress,
        "RealCity": RealCity,
        "RealCounty": RealCounty,
        "RealProvince": RealProvince,
        "tripinfolist": []
  }
    response = requests.post(url = commitUrl,json = data,headers = headers)
    return response.json()


if __name__ == '__main__':
    pass
