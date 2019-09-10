from django.shortcuts import render
from random import randint

# Create your views here.
from django_redis import get_redis_connection
from rest_framework.response import Response
from celery_tasks.sms_code.tasks import send_sms_code
from rest_framework.views import APIView

from libs.yuntongxun.sms import CCP


class SMS_Code_View(APIView):

    def get(self, request, mobile):
        # 获取参数即手机号
        # 验证手机号
        # 判断请求的间隔
        conn = get_redis_connection('sms_code')
        flag = conn.get("sms_code_flag_%s" % mobile)
        # if flag:
        #     return Response({'error': '请求过于频繁'}, status=403)

        # 生成短信验证码
        sms_code = "%06d" % randint(0, 999999)
        # 储存到redis
        conn = get_redis_connection('sms_code')
        pl = conn.pipeline()
        pl.setex("sms_code_%s" % mobile, 300, sms_code)
        # 写入一个标志数据
        pl.setex("sms_code_flag_%s" % mobile, 60, 2)
        pl.execute()
        # 发送短信
        # ccp = CCP()
        # ccp.send_template_sms(mobile, [sms_code, '5'], 1)
        send_sms_code.delay(mobile, sms_code)

        # 返回结果
        return Response("OK")
