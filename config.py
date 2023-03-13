
SECRET_KEY = "asdjjfoiajiodjaas;lf"

# 数据库配置信息
HOSTNAME = '127.0.0.1'
PORT = 3306
DATABASE = 'wenda'
USERNAME = 'root'
PASSWORD = '123456'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)


# 邮箱配置
MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "2291520961@qq.com"
MAIL_PASSWORD = "wxddrxnboymqecje"
MAIL_DEFAULT_SENDER = "2291520961@qq.com"
