# -*- coding: utf-8 -*-
"""
@Time ： 2020/7/2 上午10:43
@Auth ： LX
@File ：middlewares.py
@IDE ：PyCharm
@DES : 中间件
"""

from django.utils.deprecation import MiddlewareMixin
"""
用于解决浏览器的跨域问题
"""
class CorsMiddlewarse(MiddlewareMixin):
    def process_response(self,_,response):
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "*"
        response["Access-Control-Allow-Headers"] = "*"
        return response