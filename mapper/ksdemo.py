import requests
import os

class KSClient(object):
    def __init__(self):
        self.username = ''
        self.Token = ''
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    #获取taken
    def GetTaken(self,username,passord):
        brtn = False
        r = requests.get('http://api.95man.com:8888/api/Http/UserTaken?user='+ username +'&pwd='+ passord +'&isref=0', headers=self.headers)
        arrstr = r.text.split('|')
        if(arrstr[0] == '1'):   
            self.username = username
            self.Token = arrstr[1]
            brtn = True
        return brtn

    #识别图片
    def PostPic(self, filepath, codetype):
        strRtn = ''
        imbyte = open(filepath, 'rb').read()
        filename = os.path.basename(filepath)

        files = {'imgfile': (filename, imbyte)}
        r = requests.post('http://api.95man.com:8888/api/Http/Recog?Taken='+self.Token+'&imgtype='+ str(codetype) +'&len=0', 
                            files=files, 
                            headers=self.headers)
                            
        arrstr = r.text.split('|')
        #返回格式：识别ID|识别结果|用户余额
        if(int(arrstr[0]) > 0):   
            strRtn = arrstr[1]   
        return strRtn

if __name__ == '__main__':
    pass
