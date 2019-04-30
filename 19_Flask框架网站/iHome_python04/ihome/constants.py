
# 图片验证码的 redis 有效期，单位：秒

IMAGE_CODE_REDIS_EXPIRES = 180

# 短信验证码的 redis 有效期， 单位：秒
SMS_CODE_REDIS_EXPIRES = 300

# 发送短信验证码的redis 有效期，单位：秒
SEND_SMS_CODE_INTERVAL = 60

# 登录错误尝试次数
LOGIN_ERROR_MAX_TIMES = 5

# 登录错误限制的时间, 单位：秒
LOGIN_ERROR_FORBID_TIME = 600

# 设置fdfs存储服务器上nginx的IP和端口号
FDFS_URL = 'http://10.2.90.78:8888/'

# 设置fdfs使用的client.conf文件路径
FDFS_CLIENT_CONF = './utils/client.conf'
