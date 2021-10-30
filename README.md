# <img src="https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=69948112,3892466283&fm=26&gp=0.jpg" alt="hnu" width = "80" height = "77" /> HNU 自动打卡 HealthCheck

- 2021/10/29/ 更新 :bulb:

完善了分支管理，优化了程序环境部署，增加了ascii艺术字。

- 简介 :bulb:

> HealthCheck基于**python**搭建，它每天尝试三次打卡，成功后会**邮箱提醒**你打卡成功; 如果3次尝试仍未成功，HealthCheck会邮件提醒您手动打卡，并将**错误日志**发送给开发者（yourself）.
>
> HealthCheck分离代码和配置文件，你可以很方便地通过修改配置文件来达到**切换运行**环境的目的。同时你也可以通过向用户列表文件中添加新的打卡用户信息来进行**批量打卡**。mapper文件夹下的接口与主程序分离，可以随时**测试接口**。
>
> HealthCheck通过ASP定时框架来实现定点打卡，一旦你将HealthCheck部署到服务器，即可解放双手，高效生活。

- **声明** :triangular_flag_on_post:
> **使用此项目完成打卡的同学有义务保证信息的准确性！如若出现身体异常，请务必配合疫情防控工作，完成异常信息上报！**

- **目录结构 :trident:**

>  目录结构
```zsh
.
├── config						
│   └── appConfig.py            # 配置文件
├── data
│   ├── .img                    # 验证码图片缓存
│   └── user.csv                # 打卡用户信息         
├── main.py                      # 程序入口
├── mapper                       # 方法接口
│   ├── commit.py               # 提交打卡信息表单
│   ├── getImage.py             # 下载保存验证码图片
│   ├── ksdemo.py               # 验证码图像识别
│   ├── login.py                # 登陆
│   ├── readData.py             # 数据读取
│   └── sendEmail.py            # 邮件发送
├── README.md                    # README
└── requirements.txt             # 安装依赖
```

## Quick Start

>  使用此程序需要简单三步，在开始之前你应该使用**git clone** 或下载 **zip** 包以获取程序

### （1）环境搭建

- 解释器

```zsh
python 3.x
```

- 安装依赖

```zsh
pip install -r requirements.txt 
```

- 代发邮箱开启`POP3/SMTP`服务：

此程序包含邮箱提醒功能，如果你想要使用此功能，请将代发邮箱开启`POP3/SMTP`服务。参考教程：https://jingyan.baidu.com/article/6079ad0eb14aaa28fe86db5a.html ，注意开启服务后将会获取一段**授权码**，请保留。

- 注册**快识别**帐号：

由于采用了验证码的验证方式，所以我们要识别验证码图片，最简单的方法是用第三方API。**快识别** 免费提供了这样的服务。我们需要注册快识别的帐号来支持验证码图片识别功能，快识别官网：http://fast.95man.com/ （建议不要滥用）

### （2）填写配置文件

配置文件包含程序运行所需要的所有信息，路径为`HealthCheck/config/appConfig.py`，下面是`appConfig`的一个配置样例，你需要根据自己的使用请情况修改以下`×××`的部分：

```python
# URL
tokenURL = "https://fangkong.hnu.edu.cn/api/v1/account/getimgvcode"
imageURL = "https://fangkong.hnu.edu.cn/imagevcode"
loginUrl = 'https://fangkong.hnu.edu.cn/api/v1/account/login'
commitUrl= 'https://fangkong.hnu.edu.cn/api/v1/clockinlog/add' 

# path
dirPath  = './data/.img/'
dataPath = './data/user.csv'	# 用户帐号信息读取路径 

# 邮箱配置
senderEmail = '×××'		# 代发邮箱（使用此邮箱给打卡用户发送邮件）
sender = "×××"			# 代发邮箱昵称，任意
devEmail = '×××'		# 开发者邮箱（如出现打卡失败的情况，代发邮箱给此邮箱发送打卡失败用户列表）
AuthCode = '×××'		# 开启`POP3/SMTP`服务时的授权码
port = 587                 # stmp使用端口

sucessMsg = '   今日打卡成功，打卡时间：'
failMsg = '     我们对您的账户进行了3次打卡尝试，由于某些原因导致打卡失败，请于今日手动完成打卡。\
您可以尝试联系此邮箱以解决打卡失败的问题。祝您生活愉快！\n发件人： '+senderEmail	# 请不要调整Msg之间的换行和空格

# http://fast.95man.com/注册使用
k95Username = '×××'		# 快识别帐号
k95Passwd = "×××"		# 快识别密码

# 打卡时间设置 0:20
checkHour = '0'			   # 时间设置 任意
checkMin  = '20'
```

### （3）填写打卡用户信息

程序已配置完毕，接下来填写打卡用户信息。你需要修改路径`HealthCheck/data/user.csv` 文件，参考以下实例：
- 2021/3/3更新

```python
username,passwd,email,RealAddress,RealCity,RealCounty,RealProvince,BackState,MorningTemp,NightTemp
2018*******2,****,***@qq.com,湖南大学天马学生公寓3区11栋***,长沙市,岳麓区,湖南省,1,36.3,36.3
.....继续添加新用户
```

> 注意：username,passwd分别代表`Ge ren men hu`帐号和密码。

## 运行实例

- 最后，你可以简单的使用命令执行`main.py`来运行程序

```zsh
$ python main.py
##   ##  #######    ###    ##     ######  ##   ##            #####   ##   ##  #######   #####   ##   ##  
##   ##  ##        ## ##   ##       ##    ##   ##           ##   ##  ##   ##  ##       ##   ##  ##  ##   
##   ##  ##       ##   ##  ##       ##    ##   ##           ##       ##   ##  ##       ##       ## ##    
#######  #####    ##   ##  ##       ##    #######           ##       #######  #####    ##       ####     
##   ##  ##       #######  ##       ##    ##   ##           ##       ##   ##  ##       ##       ## ##    
##   ##  ##       ##   ##  ##       ##    ##   ##           ##   ##  ##   ##  ##       ##   ##  ##  ##   
##   ##  #######  ##   ##  #######  ##    ##   ##            #####   ##   ##  #######   #####   ##   ##  

----------[log] : 2021-10-29 15:40:43
获取token: d5ea1ad132eb446aac0a9d88452a9237
Download image 2018080105222.jpeg sucessfully
........
```

- **终端日志**

<img src="https://i.loli.net/2021/03/03/OMqYyjT8LGKtsVN.png" alt="image-20210303163907838" style="zoom: 55%;" />  

- **邮箱提醒**

<img src="https://i.loli.net/2021/02/12/ClmSj6RqrnO9JeB.png" alt="image-20210212142621554" width = "400"/> <img src="https://i.loli.net/2021/02/12/mzMoVOyfSdWlH48.png" alt="image-20210212142659234" width = "400" />

<img src="https://i.loli.net/2021/02/13/6xBdGVJEKqUeR1g.png" alt="image-20210213131631644" width = "400" /> （开发者dev）

## 部署服务器（非必须）

如果将HealthCheck部署到服务器，你就能完全解放双手了，部署方法如下：


```zsh
# 在服务器上克隆项目
git clone git@github.com:LinXiaoDe/HealthCheck.git

# 修改配置文件和用户列表
参考 $quickSatart

# 开启一个screen会话
screen -S HealthCheck

# 进入根目录
cd HealthCheck

# 执行
python main.py
```
- 注意:warning: ：

阿里云或者腾讯云一般未开放stmp功能的默认端口，这意味着你在本地电脑上可以通过邮箱测试，部署到云端则会出现错误。因此在服务器部署时，安全组一定要放行stmp端口。本教程中使用阿里云，qq邮箱，端口为`587`，请在安全组中放行`587`.

