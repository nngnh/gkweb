# -*- coding: utf-8 -*-
"""
@Time ： 2020/7/1 下午4:07
@Auth ： LX
@File ：forecast.py
@IDE ：PyCharm
@DES : 预测
"""
import pandas as pd
from django.core.cache import cache
from web.utils.serializers import *
from GkWeb import settings

def get_avglocal(sciLinedf):
    '''
    #获取近几年的平均位次
    :param sciLinedf: 学校调档线位次的dataframe
    :return: 进行聚类和排序后的数据
    '''
    # 获取到近几年的位次
    sciLineLocation = sciLinedf[
        ['collegeCode', 'collegeHistoryId', 'province', 'collegeName', 'subject', 'sequence', 'year',
         'moveDocLocation']]
    # 拿到2016-2018的数据
    sciLineData = sciLineLocation[sciLineLocation['year'].isin([2016, 2017, 2018])]
    #进行聚类，得到平均的录取位次
    data = sciLineData.groupby(['collegeCode', 'collegeHistoryId', 'province', 'collegeName', 'subject', 'sequence',],
                               as_index=False).agg({'moveDocLocation': 'mean'})
    # 先对历史数据按照平均 moveDocLocation 排序
    data = data.sort_values(['moveDocLocation'], ascending=True)
    # 重置索引
    data.index = range(data.shape[0])
    return data


def get_sciYiFenYiDuan(year):
    '''
    # 获取到当年的一分一段表
    :param year:年
    :return:返回一分一段表的dataframe
    '''
    sciYiFen = SciYiFenYiDuan.objects.filter(year=year)
    sciYiFenList = list(sciYiFen.values())
    yiFenYiDuan = pd.DataFrame(sciYiFenList)
    return yiFenYiDuan

def get_artYiFenYiDuan(year):
    '''
    获取文科学校的一分一段表
    :param year:
    :return:
    '''
    artYiFen = ArtYiFenYiDuan.objects.filter(year=year)
    artYiFenList = list(artYiFen.values())
    yiFenYiDuan = pd.DataFrame(artYiFenList)
    return yiFenYiDuan

def compute_rank(score,yiFenYiDuan):
    '''
    根据分数和一分一段表查询到排名
    :param score: 分数
    :param yiFenYiDuan: 一分一段表
    :return:排名
    '''
    #获取到最高分
    max_score = int(yiFenYiDuan[:1]['score'])
    #最低排名
    min_rank = int(yiFenYiDuan[:1]['rank'])
    if score > max_score:
        return min_rank,1
    else:
        data_score = yiFenYiDuan[yiFenYiDuan['score'] == score]
        rank = int(data_score['num'] + data_score['rank'])
        return rank,min_rank


def compute_section(score,rate,rank,yiFenYiDuan,mark):
    '''
    #计算排名区间  稳，保，冲
    :param score: 分数
    :param rate: 输入的分值，比如选中稳 输入2 就是计算score-2到score+2的排名
    :param rank: 一分一段表排名
    :param yiFenYiDuan: 一分一段表
    :param mark: 稳、保、冲
    :return: 返回低排名和高排名，后续选择学校就是这两个排名之间的
    '''
    if rate < 0:
        rate = -rate
    high_rank,min_rank1 = compute_rank(score - rate,yiFenYiDuan)
    # current_rank,current_min_rank = compute_rank(score,yiFenYiDuan)
    low_rank,min_rank2 = compute_rank(score + rate,yiFenYiDuan)
    if mark=='稳':
        low = low_rank
        high = high_rank
        min_rank = min_rank2
    elif mark == '冲':
        low = low_rank
        high = rank
        min_rank = min_rank2
    else:
        low = rank
        high = high_rank
        min_rank = min_rank1
    return low,high,min_rank

def get_forecast_score(datadf,yiFenYiDuandf):
    '''
    #计算平均位次在当年的分数，相当于预测学校分数
    :param data: 前几年学校的平均位次df
    :param yiFenYiDuan:  一分一段表df
    :return:
    '''
    list_score = []
    #获取datadf中的平均位次
    for index, data in datadf.iterrows():
        for i, yiFenYiDuan in yiFenYiDuandf.iterrows():
            if data['moveDocLocation']<= yiFenYiDuan['rank']:
                list_score.append(yiFenYiDuan['score'])
                break

    datadf['forecast_score'] = list_score
    return datadf
def get_sci_paln():
    '''f
    计算理科招生计划
    :param data:
    :return:
    '''
    key = settings.REDIS_SCIPLAN
    sciPlans = cache.get(key)
    if sciPlans is None:
        plans = SciPlan.objects.filter(year=2019)
        plansList = list(plans.values())
        plansdf = pd.DataFrame(plansList)
        cache.set(key,plansdf,settings.REDIS_TIMEOUT)
    else:
        plansdf = sciPlans
    return plansdf

def forecast_sciuniverity(score,mark,rate):
    '''
    预测理科学校
    :param score:  分数
    :param mark: 稳、保、冲
    :param rate: 输入的分值，比如选中稳 输入2 就是计算score-2到score+2的排名
    :return: 返回预测学校的dataframe和低排名
    低排名用于后续预测专业
    '''
    #获得所有的学校信息
    key = 'scicollege'
    sciLine = cache.get(key)
    if sciLine is None:
        #获取大于2015年的数据
        sciCollegeLines = SciCollegeLine.objects.filter(year__gt=2015)
        sciLineList = list(sciCollegeLines.values())
        plandf = get_sci_paln()
        sciLinedf = pd.DataFrame(sciLineList)
        # 获取到平均位次
        data = get_avglocal(sciLinedf)
        #根据学校名和批次合并两个dataframe
        mergdf = pd.merge(data,plandf,on=['collegeName','sequence','province','subject'])
        cache.set(key, mergdf, settings.REDIS_TIMEOUT)
    else:
        mergdf = sciLine


    #获取到当年的一分一段表
    yiFenYiDuan = get_sciYiFenYiDuan(2019)
    # 根据分数找到当前的一分一段表排名
    rank,current_min_rank = compute_rank(score,yiFenYiDuan)
    #根据输入的rate计算出low_rank,rank,high_rank
    low,high,min_rank = compute_section(score,rate,rank,yiFenYiDuan,mark)
    if  min_rank==1 or current_min_rank ==1:
        forecast_data = mergdf[mergdf['moveDocLocation'] >= 1]
        forecast_data = forecast_data[forecast_data['moveDocLocation'] <= 1000]
        # 计算平均位次在当年的分数，相当于预测学校分数
        forecast_data = get_forecast_score(forecast_data, yiFenYiDuan)
        low=1
        #找到学校对应的招生计划
        # forecast_data = get_forecast_paln(forecast_data)
    else:
        forecast_data = mergdf[mergdf['moveDocLocation'] >= low]
        forecast_data = forecast_data[forecast_data['moveDocLocation'] <= high]
        # 计算平均位次在当年的分数，相当于预测学校分数
        forecast_data = get_forecast_score(forecast_data, yiFenYiDuan)
        # forecast_data = get_forecast_paln(forecast_data)
    return forecast_data,low

def get_arts_paln():
    '''f
    计算文科招生计划
    :param data:
    :return: df
    '''
    key = settings.REDIS_ARTSPLAN
    artsPlans = cache.get(key)
    if artsPlans is None:
        plans = ArtsPlan.objects.filter(year=2019)
        plansList = list(plans.values())
        plansdf = pd.DataFrame(plansList)
        cache.set(key,plansdf,settings.REDIS_TIMEOUT)
    else:
        plansdf = artsPlans
    return plansdf

def forecast_artuniverity(score,mark,rate):
    '''
    预测文科学校
    :param score:
    :param mark:
    :param rate:
    :return:
    '''
    #获得所有的学校信息
    key = 'artcollege'
    artLine = cache.get(key)
    if artLine is None:
        artCollegeLines = ArtsCollegeLine.objects.filter(year__gt=2015)
        artLineList = list(artCollegeLines.values())
        artLinedf = pd.DataFrame(artLineList)
        plandf = get_arts_paln()
        # 获取到平均位次
        data = get_avglocal(artLinedf)
        # 根据学校名和批次合并两个dataframe
        mergdf = pd.merge(data, plandf, on=['collegeName', 'sequence', 'province', 'subject'])
        cache.set(key, mergdf, settings.REDIS_TIMEOUT)
    else:
        mergdf = artLine


    #获取到当年的一分一段表
    yiFenYiDuan = get_artYiFenYiDuan(2019)

    # 根据分数找到当前的一分一段表排名
    rank,min_rank = compute_rank(score,yiFenYiDuan)
    #根据输入的rate计算出low_rank,rank,high_rank
    low,high,min_rank = compute_section(score,rate,rank,yiFenYiDuan,mark)
    if min_rank ==1 :
        forecast_data = mergdf[mergdf['moveDocLocation'] >= min_rank]
        forecast_data = forecast_data[forecast_data['moveDocLocation'] <= 1000]
        # 计算平均位次在当年的分数，相当于预测学校分数
        forecast_data = get_forecast_score(forecast_data, yiFenYiDuan)
        low = 1
    else:
        forecast_data = mergdf[mergdf['moveDocLocation'] >= low]
        forecast_data = forecast_data[forecast_data['moveDocLocation'] <= high]
        forecast_data = get_forecast_score(forecast_data, yiFenYiDuan)
    return forecast_data,low

def get_major_avglocal(Majorsdf,collegeCode,collegeHistoryId):
    '''
    获取到不同专业的平均录取位次
    :param Majorsdf: 专业录取线的dataframe
    :param collegeCode:  学校code
    :param collegeHistoryId:
    :return: 返回聚类和处理后的学校
    '''
    #拿到2016-2018年的数据
    # major_score = Majorsdf[Majorsdf['year'].isin([2016,2017,2018])]
    # filter_major = major_score[(major_score['collegeCode'] == collegeCode)&(major_score['collegeHistoryId'] == collegeHistoryId)]
    filter_major = Majorsdf[
        (Majorsdf['collegeCode'] == collegeCode) & (Majorsdf['collegeHistoryId'] == collegeHistoryId)]
    major_score = filter_major[filter_major['year'].isin([2016,2017,2018])]
    # 按照专业名称聚类，查找平均位次
    data = major_score.groupby(['collegeCode', 'collegeHistoryId', 'collegeName', 'sequence', 'speicaltyName'],
                                as_index=False).agg({'matricGradePosition': 'mean'})
    return data

def get_major_forecast_score(datadf,yiFenYiDuandf):
    '''
    预测专业录取分数
    :param datadf:
    :param yiFenYiDuan:
    :return:
    '''
    datadf.index = range(datadf.shape[0])
    df = datadf
    list_score = []
    # 获取datadf中的平均位次
    for index, data in datadf.iterrows():
        for i, yiFenYiDuan in yiFenYiDuandf.iterrows():
            if data['matricGradePosition'] <= yiFenYiDuan['rank']:
                list_score.append(yiFenYiDuan['score'])
                break
    df['forecast_score'] = list_score
    return df

def forecast_scimajor(collegeCode,collegeHistoryId,low_rank):
    '''
    预测理科专业
    :param collegeCode:
    :param collegeHistoryId:
    :param low_rank: 上面预测学校的返回的低排名
    :return: 预测学校的dataframe，这里还需要处理，不足6个专业，需要补充，因为一个学校可以填6个专业
    '''
    key = 'scimajor'
    sciMajor = cache.get(key)
    if sciMajor is None:
        sciMajors = SciMajorLine.objects.filter(year__gt=2015)
        sciMajorsList = list(sciMajors.values())
        sciMajorsdf = pd.DataFrame(sciMajorsList)
        cache.set(key,sciMajorsList,settings.REDIS_TIMEOUT)
    else:
        sciMajorsdf = pd.DataFrame(sciMajor)

    data = get_major_avglocal(sciMajorsdf,collegeCode,collegeHistoryId)
    #预测的专业
    forecast_data = data[data['matricGradePosition'] >= low_rank]
    forecast_data = forecast_data.sort_values('matricGradePosition')
    #剩余的专业
    other_data = data[data['matricGradePosition'] < low_rank]

    yiFenYiDuan = get_sciYiFenYiDuan(2019)

    if len(forecast_data)==0:
        #code = 1 表示都不是预测的
        other_data['code'] = 1
        data = other_data
    elif len(other_data) == 0:
        #code = 0 表示学校是预测的
        forecast_data['code'] = 0
        #如果预测大于6个专业，直接返回
        if len(forecast_data) > 6:
            output_data = get_major_forecast_score(forecast_data,yiFenYiDuan)
            return output_data
        else:
            data = forecast_data
    else:
        forecast_data['code'] = 0
        other_data['code'] = 1
        if len(forecast_data) > 6:
            output_data = get_major_forecast_score(forecast_data, yiFenYiDuan)
            return output_data
        else:
            data = pd.concat([forecast_data, other_data], axis=0)

    if len(data) <= 6:
        output_data = get_major_forecast_score(data, yiFenYiDuan)
        return output_data
    else:
        output_data = get_major_forecast_score(data[:6], yiFenYiDuan)
        return output_data


def forecast_artsmajor(collegeCode,collegeHistoryId,low_rank):
    '''
    预测文科专业
    :param collegeCode:
    :param collegeHistoryId:
    :param low_rank:
    :return:
    '''
    key = 'artsmajor'
    artsMajor = cache.get(key)
    if artsMajor is None:
        artsMajors = ArtsMajorLine.objects.filter(year__gt=2015)
        artsMajorsList = list(artsMajors.values())
        artsMajorsdf = pd.DataFrame(artsMajorsList)
        cache.set(key,artsMajorsList,settings.REDIS_TIMEOUT)
    else:
        artsMajorsdf = pd.DataFrame(artsMajor)

    data = get_major_avglocal(artsMajorsdf,collegeCode,collegeHistoryId)
    forecast_data = data[data['matricGradePosition'] >= low_rank]
    forecast_data = forecast_data.sort_values('matricGradePosition')
    #剩余的学校
    other_data = data[data['matricGradePosition'] < low_rank]
    yiFenYiDuan = get_artYiFenYiDuan(2019)
    if len(forecast_data) == 0:
        # code = 1 表示都不是预测的
        other_data['code'] = 1
        data = other_data
    elif len(other_data) == 0:
        # code = 0 表示学校是预测的
        forecast_data['code'] = 0
        # 如果预测大于6个专业，直接返回
        if len(forecast_data) > 6:
            output_data = get_major_forecast_score(forecast_data, yiFenYiDuan)
            return output_data
        else:
            data = forecast_data
    else:
        forecast_data['code'] = 0
        other_data['code'] = 1
        if len(forecast_data) > 6:
            output_data = get_major_forecast_score(forecast_data, yiFenYiDuan)
            return output_data
        else:
            data = pd.concat([forecast_data, other_data], axis=0)
    if len(data) <= 6:
        output_data = get_major_forecast_score(forecast_data, yiFenYiDuan)
        return output_data
    else:
        output_data = get_major_forecast_score(data[:6], yiFenYiDuan)
        return output_data


