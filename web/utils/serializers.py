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


#学校信息序列化不包括introduce
class CollegeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeInfo
        fields = ['collegeCode', 'collegeName', 'categoryName', 'propertyName', 'levelName', 'provinceName', 'cityName',
                  'address', 'url', 'phone']
#学校信息序列化，包括introduce
class CollegeInfoAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeInfo
        fields = "__all__"

#理科调档线序列化,部分数据
class SciCollegeLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = SciCollegeLine
        fields = ['collegeCode','collegeHistoryId','province','collegeName','subject','sequence']
#理科调档线序列化,所有数据
class SciCollegeLineAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = SciCollegeLine
        fields = '__all__'
#文科调档线序列化,部分数据
class ArtsCollegeLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtsCollegeLine
        fields = ['collegeCode','collegeHistoryId','province','collegeName','subject','sequence']
#文科调档线序列化,所有数据
class ArtsCollegeLineAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtsCollegeLine
        fields = '__all__'
#批次
class OrderAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

#用户
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
#省份
class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'

#理科专业
class SciMajorLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = SciMajorLine
        fields = '__all__'
#文科专业
class ArtsMajorLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtsMajorLine
        fields = '__all__'
#专业实力
class MajorAbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = MajorAbility
        fields = '__all__'
#理科录取情况
class SciEnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = SciEnroll
        fields = '__all__'
#文科录取情况
class ArtsEnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtsEnroll
        fields = '__all__'
#招生简章
class EnrollmentGuldeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnrollmentGulde
        fields = '__all__'

#专业库
class MajorInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MajorInfo
        fields = '__all__'

