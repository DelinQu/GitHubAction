# URL
tokenURL = "https://fangkong.hnu.edu.cn/api/v1/account/getimgvcode"
imageURL = "https://fangkong.hnu.edu.cn/imagevcode"
loginUrl = 'https://fangkong.hnu.edu.cn/api/v1/account/login'
commitUrl= 'https://fangkong.hnu.edu.cn/api/v1/clockinlog/add' 

# path
dirPath  = './data/.img'

# 邮箱配置
senderEmail = 'qdl.no-reply@foxmail.com'
sender = "qdl-dev"
devEmail = 'qdl.no-reply@foxmail.com'
AuthCode = 'nprgjutnqcdedhdc'
sucessMsg = '   今日打卡成功，打卡时间：'
failMsg = '     我们对您的账户进行了3次打卡尝试，由于某些原因导致打卡失败，请于今日手动完成打卡。\
您可以尝试联系此邮箱以解决打卡失败的问题。祝您生活愉快！\n发件人： '+senderEmail                    # 格式无需调整

# http://fast.95man.com/注册使用
k95Username = 'qdl-dev'
k95Passwd = 'qdl-dev'

# 用户信息
RealAddress,RealCity,RealCounty,RealProvince,BackState,MorningTemp,NightTemp = \
	"湖南大学","长沙市","岳麓区","湖南省",1,36.3,36.3

# ascii 字符
asciiText = ""\
    "##   ##  #######    ###    ##     ######  ##   ##            #####   ##   ##  #######   #####   ##   ##  \n" \
    "##   ##  ##        ## ##   ##       ##    ##   ##           ##   ##  ##   ##  ##       ##   ##  ##  ##   \n" \
    "##   ##  ##       ##   ##  ##       ##    ##   ##           ##       ##   ##  ##       ##       ## ##    \n" \
    "#######  #####    ##   ##  ##       ##    #######           ##       #######  #####    ##       ####     \n" \
    "##   ##  ##       #######  ##       ##    ##   ##           ##       ##   ##  ##       ##       ## ##    \n" \
    "##   ##  ##       ##   ##  ##       ##    ##   ##           ##   ##  ##   ##  ##       ##   ##  ##  ##   \n" \
    "##   ##  #######  ##   ##  #######  ##    ##   ##            #####   ##   ##  #######   #####   ##   ##  \n"
