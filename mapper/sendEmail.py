from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText

def sendEmail(sender,receivers,AuthCode,fromUser,toUser,head,content):
    port = 587                      # stmp使用端口
    message = MIMEText(content, _subtype='plain', _charset='utf-8')
    message['From'] = Header(fromUser, 'utf-8')
    message['To'] = Header(toUser, 'utf-8')
    message['Subject'] = Header(head, 'utf-8')
    smtper = SMTP('smtp.qq.com',port=port,timeout=10)

    # QQ邮箱smtp的授权码
    smtper.login(sender, AuthCode)  
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成!')

if __name__ == '__main__':
    pass