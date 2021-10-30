import os
from mapper.getImage import getToken,getPic
from mapper.ksdemo import KSClient
from mapper.login import login
from mapper.sendEmail import sendEmail
from mapper.commit import commit
import time
from config.appConfig import *

# 打卡
def check(username,passwd,RealAddress,RealCity,RealCounty,RealProvince,BackState,MorningTemp,NightTemp):
    imageName = username+".jpeg"
    # 获取&下载图片
    token = getToken(tokenURL)
    print("获取token:",token)
    if(token != "error"):
        url = imageURL + "?token=" + token
        getPic(url,dirPath,imageName)
    # 获取验证码
    Ks95man = KSClient()
    verCode = ""
    if Ks95man.GetTaken(k95Username,k95Passwd):
        verCode = Ks95man.PostPic(dirPath+imageName,2)
        print('识别结果：'+verCode)
    # 登陆
    response,cookie= login(loginUrl,username,passwd,token,verCode)
    if response['code'] != 0:   # 登陆失败
        return -1
    print("登陆成功")
    # 提交信息
    response = commit(commitUrl,RealAddress,RealCity,RealCounty,RealProvince,BackState,MorningTemp,NightTemp,cookie)
    print(response)
    return response['code']

# 循环打卡作业 [这里重用了master中的代码，由于github action secrity有限的缘故，只能打卡单个用户]
def check_Job():
    cur = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
    print("----------[log] : "+cur)
    username,passwd,email = os.environ["USERNAME"],os.environ["PASSWD"],os.environ["EMAIL"]
    # 最多进行3次打卡尝试 per day
    isCheck = 0
    for t in range(3):
        try:
            res = check(username,passwd,RealAddress,RealCity,RealCounty,RealProvince,BackState,MorningTemp,NightTemp)
        except:
            res = -1
        cur = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        # 打卡成功
        if(res == 0):
            sendEmail(senderEmail,email,AuthCode,sender,username,
			"打卡成功提醒","Hi "+username+" :\n"+sucessMsg+cur+"，祝您生活愉快！\n发件人： "+senderEmail)
            isCheck = 1
        # 重复打卡
        elif(res == 1):
            isCheck = 1

    # 未成功打卡的用户发送邮箱提醒手动打卡
    if(isCheck==0):
            print("打卡失败，请手动打卡或重试！")
            cur = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
            sendEmail(senderEmail,email,AuthCode,
                      sender,username,"打卡失败提醒","Hi "+username+" ：\n"+failMsg)
            # 开发者邮件
            sendEmail(senderEmail,devEmail,AuthCode,sender,'Developer',
                      "打卡失败提醒(dev)","打卡出现问题，下列用户未打卡"+email)

if __name__ == '__main__':
    print(asciiText)
    check_Job()