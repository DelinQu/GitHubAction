import requests
import os
# URL和目录
# tokenURL = "https://fangkong.hnu.edu.cn/api/v1/account/getimgvcode"
# imageURL = "https://fangkong.hnu.edu.cn/imagevcode"
# dirPath  = "../data/.img"

# 获取图片token
def getToken(url):
    try:
        # get请求，转json格式
        reponse=requests.get(url).json()
        # reponse=requests.get(url,allow_redirects=False)
        # print(reponse.cookies)
        # 这里没有cookie
        return reponse["data"]["Token"]
    except:
        return 'error'

# 下载保存图片
def getPic(url,path,name):
    fullPath = path + name 
    if not os.path.exists(path):
        os.mkdir(path)
    # 下载验证图片 直接替换
    # if not os.path.exists(fullPath):
    r=requests.get(url)
    f=open(fullPath,'wb')
    f.write(r.content)
    f.close()
    print('Download image ' + name +" sucessfully")

# if __name__ == '__main__':
#     for i in range(10):
#         token = getToken(tokenURL)
#         print(i,token)
#         if(token != "error"):
#             url = imageURL + "?token=" + token
#             getPic(url,dirPath,str(i)+".jpeg")
