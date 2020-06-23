# -*- coding: utf-8 -*-
"""
@Time ： 2020/6/22 下午7:46
@Auth ： LX
@File ：serializers.py
@IDE ：PyCharm
@DES :  序列化
"""

from rest_framework import serializers
from web.models import *

#理科专业分数线序列化字段
class SciMajorLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = SciMajorLine
        fields = "__all__"