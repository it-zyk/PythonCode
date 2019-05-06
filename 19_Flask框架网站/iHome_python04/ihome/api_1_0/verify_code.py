from . import api
from ihome.utils.captcha.captcha import captcha
from ihome import redis_store, constants
from flask import current_app, jsonify, make_response, request
from ihome.utils.response_code import RET
from ihome.models import User
# from ihome.libs.yuntongxun.sms import CCP
from ihome.libs.yixintong.sms import SMSSend
import random
from ihome.tasks.task_sms import send_sms

# GET 127.0.0.1/api/v1.0/image_code/<image_code_id>


@api.route("/image_codes/<image_code_id>")
def get_image_code(image_code_id):
    """
    获取图片验证
    :params image_code_id: 图片验证码编号
    ;return 验证图片
    """
    # 1.获取参数

    # 2. 检验参数
    # 3. 业务逻辑处理
    # a.生产验证码图片
    name, text, image_data = captcha.generate_captcha()
    """
    # b.将验证码真实值与编号保存在redis 中,设置有效期
    # Redis： string, list, hash, set, zset
    # "image_code":{"编号1":"真实文本”， "id2":"",} hash : hset("image_code",
    # "id1"
    # 单条维护记录，选用字符串

    # "image_code_编号" : "真实值"
    # redis_store.set("image_code_%s" % image_code_id, text)
    # redis_store.expire("image_code_%s" % image_code_id,
    # constants.IMAGE_CODE_REDIS_EXPIRES)  # 3分钟有效期
    """
    try:
        redis_store.setex("image_code_%s" % image_code_id,
                          constants.IMAGE_CODE_REDIS_EXPIRES, text)
    except Exception as e:
        # 记录日志
        current_app.logger.error(e)
        return jsonify(error=RET.DBERR, errmsg="保存图片验证码失败")

    # 4.返回值
    resp = make_response(image_data)
    resp.headers["Content-Type"] = "image/jpg"
    return resp


# GET /api/v1.0/sms_codes/<mobile>?image_code=xxxx&image_code_id=xxxx
@api.route("/sms_codes/<re(r'1[34578]\d{9}'):mobile>")
def get_sms_code(mobile):
    """ 获取短信验证码 """
    # 获取参数
    image_code = request.args.get("image_code")
    image_code_id = request.args.get("image_code_id")

    # 校验
    if not all([image_code, image_code_id]):
        # 表示参数不完整
        return jsonify(error=RET.PARAMERR, errmsg="参数不完整")

    # 业务逻辑处理
    # 从redis 中取出真实的图片验证码

    try:
        real_image_code = redis_store.get("image_code_%s" % image_code_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="redis数据库异常")

    # 判断验证码是否过期
    if real_image_code is None:
        # 表示图片没有或者过期
        return jsonify(errno=RET.NODATA, errmsg="图片验证码失效")

    # 删除redis 中的图片验证码, 防止用户使用同一个图片验证码验证多次
    try:
        redis_store.delete("image_code_%s" % image_code_id)
    except Exception as e:
        current_app.logger.error(e)

    if real_image_code.decode().lower() != image_code.lower():
        # 表示用户填写验证码错误
        return jsonify(error=RET.DATAERR, errmsg="图片验证码错误")

    # 判断对于这个手机号的操作，在60秒内有没有记录，如果有，则认为用户操作频繁，不接受处理
    try:
        send_flag = redis_store.get("send_sms_code_%s" % mobile)
    except Exception as e:
        current_app.logger.error(e)
    else:
        if send_flag is not None:
            # 表示60秒内有过发送记录
            return jsonify(errno=RET.REQERR, errmsg="请求过于频繁，请60秒后重试")

    # 判断手机号是否存在
    try:
        user = User.query.filter_by(mobile=mobile).first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="redis 数据库异常")
    else:
        if user is not None:
            # 表示手机号已经存在
            return jsonify(errno=RET.DATAEXIST, errmsg="手机已存在")

    # 如果手机号不存在， 则生产短信验证码
    sms_codes = "%06d" % random.randint(0, 999999)

    # 保存真实的短信验证码
    try:
        redis_store.setex("sms_code_%s" % mobile,
                          constants.SMS_CODE_REDIS_EXPIRES, sms_codes)
        # 保存发送给这个手机号的记录，防止用户在60s内再次发送短信的操作
        redis_store.setex("send_sms_code_%s" %
                          mobile, constants.SEND_SMS_CODE_INTERVAL, 1)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="保存短信码异常")

    # 发送短信
    # try:
    #     ccp = SMSSend()
    #     # sms_info_dic = [sms_codes, int(constants.SMS_CODE_REDIS_EXPIRES/63)]
    #     # result = ccp.send_template_sms(mobile, sms_info_dic)
    #     sms_data_info = "您的登陆验证码是：%s"  % sms_codes
    #     result = ccp.send_message_info(mobile, sms_data_info)
    # except Exception as e:
    #     current_app.logger.error(e)
    #     return jsonify(errno=RET.THIRDERR, errmsg="发送异常")
    sms_data_info = "您的登陆验证码是：%s" % sms_codes
    send_sms.delay(mobile,  sms_data_info)
    return jsonify(errno=RET.OK, errmsg="发送成功")

    # if result == 0:
    #     # 发送成功
    #     return jsonify(errno=RET.OK, errmsg="发送成功")
    # else:
    #     return jsonify(error=RET.THIRDERR, errmsg="发送失败")
    #
    # if result == 0:
    #     # 发送成功
    #     return jsonify(errno=RET.OK, errmsg="发送成功")
    # else:
    #     return jsonify(errno=RET.THIRDERR, errmsg="发送失败")
    #
    # 业务逻辑处理
    # 1.从redis 数据中取数据
    # 2.与用户填写的值进行
    # 返回值
