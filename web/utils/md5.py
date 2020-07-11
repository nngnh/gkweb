# -*- coding: utf-8 -*-
"""
@Time ： 2020/6/30 下午5:11
@Auth ： LX
@File ：md5.py
@IDE ：PyCharm
@DES : 对密码进行md5加密
"""
import hashlib

def password_md5(pwd):
    md5 = hashlib.md5()  #实例化md5
    md5.update(pwd.encode())   #对字符串的字节类型加密
    result = md5.hexdigest()  #加密
    return result
