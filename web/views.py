from django.shortcuts import render
from django.core.cache import cache
from rest_framework import views
from rest_framework import response
from web.models import *
from web.utils.serializers import *
from GkWeb import settings
from web.utils.forecast import *
import uuid
from web.utils import md5
import numpy as np

#学校信息列表
class CollegeInfoListView(views.APIView):
    def get(self,request):
        msg = {'code':1,'data':[]}
        #查询所有
        try:
            key = settings.REDIS_COLLEGEINFO
            data = cache.get(key)
            if data is None:
                collegeInfos = CollegeInfo.objects.all()
                serializer = CollegeInfoSerializer(collegeInfos, many=True)
                cache.set(key,serializer.data,settings.REDIS_TIMEOUT)
                msg['code'] = 0
                msg['data'] = serializer.data
            else:
                msg['code'] = 0
                msg['data'] = data
            return response.Response(msg)
        except:
            return response.Response(msg)

    def post(self,request):
        '''
        查询学校信息，返回按条件查询信息
        :param request:
        :return:
        '''
        msg = {'code': 1, 'data': []}
        try:
            province = request.data.get('province')
            #院校类型
            subject = request.data.get('subject')
            #输入的关键字，模糊查询学校名称
            collegeName = request.data.get('key')
            key = settings.REDIS_COLLEGEINFO
            collegeInfos = cache.get(key)

            collegeInfoList = list(collegeInfos)
            collegeInfodf = pd.DataFrame(collegeInfoList)
            if province is not None and province != '':
                province = province.split(',')
                collegeInfodf = collegeInfodf[collegeInfodf['provinceName'].isin(province)]
            if subject is not None and subject != '':
                collegeInfodf = collegeInfodf[collegeInfodf['categoryName'] == subject]
            if collegeName is not  None and collegeName != '':
                #模糊查询
                collegeInfodf = collegeInfodf[collegeInfodf['collegeName'].str.contains(collegeName)]
            data_list = []
            for index, data in collegeInfodf.iterrows():
                item = {'collegeCode': data['collegeCode'], 'collegeName': data['collegeName'],
                        'categoryName': data['categoryName'], 'propertyName': data['propertyName'],
                        'levelName': data['levelName'],'provinceName': data['provinceName'],
                        'cityName': data['cityName']}
                data_list.append(item)
            msg['code'] = 0
            msg['data'] = data_list
            return response.Response(msg)
        except:
            return response.Response(msg)
#学校信息(单条数据)
class CollegeInfoView(views.APIView):
    def get(self,request,pk):
        msg = {'code':1,'data':[]}
        try:
            collegeInfo = CollegeInfo.objects.filter(collegeCode = pk).first()
            serializer = CollegeInfoAllSerializer(collegeInfo,many=False)
            msg['code'] = 0
            msg['data'] = serializer.data
            return response.Response(msg)
        except:
            return response.Response(msg)
#理科调档学校信息 这里返回部分数据，用于列表显示
class SciCollegeLineListView(views.APIView):
    def get(self,request):
        '''
        查询理科所有学校不同的录取批次，比如清华大学有本一批和提前批就显示两条数据
        :param request:
        :return:
        '''
        msg = {'code': 1, 'data': []}
        try:
            key = settings.REDIS_ALLSCICOLLEGELINE
            data = cache.get(key)
            if data is None:
                SciCollegeLines = SciCollegeLine.objects.all()
                serializer = SciCollegeLineAllSerializer(SciCollegeLines,many=True)
                cache.set(key, serializer.data, settings.REDIS_TIMEOUT)
                datadf = pd.DataFrame(serializer.data)
            else:
                datadf = pd.DataFrame(data)
            # 默认为2019年数据
            datadf = datadf[datadf['year'] == 2019]
            datadf = datadf.sort_values(by=['moveDocGrade'], ascending=False)
            # 数据中有NAN，json不能转换，需要处理W为‘’
            datadf = datadf.fillna('')
            data_list = []
            for index, data in datadf.iterrows():
                item = {'collegeCode': data['collegeCode'], 'collegeHistoryId': data['collegeHistoryId'],
                        'collegeName': data['collegeName'], 'province': data['province'],
                        'subject': data['subject'], 'sequence': data['sequence'],
                        'moveDocGrade': data['moveDocGrade'], 'averageGrade': data['averageGrade'],
                        'moveDocGradeDiff': data['moveDocGradeDiff'], 'averageGradeDiff': data['averageGradeDiff'],
                        'moveDocLocation': data['moveDocLocation'], 'averageLocation': data['averageLocation'],
                        'year': '2019'}
                data_list.append(item)
            msg['code'] = 0
            msg['data'] = data_list
            return response.Response("msg")
            # return response.Response(msg)
        except:
            return response.Response(msg)

    def post(self,request,*args,**kwargs):
        '''
        按照输入的条件查询理科
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        msg = {'code': 1, 'data': []}
        try:
            province = request.data.get('province')
            collegeName = request.data.get('key')
            sequence = request.data.get('sequence')
            score = request.data.get('score')
            year = request.data.get('year')
            key = settings.REDIS_ALLSCICOLLEGELINE
            data = cache.get(key)
            if score is None or score == '':
                if data is None:
                    return response.Response(msg)
                else:
                    datadf = pd.DataFrame(data)
                if sequence is not None and sequence != '':
                    datadf = datadf[datadf['sequence'] == sequence]
                if province is not None and province != '':
                    province = province.split(',')
                    datadf = datadf[datadf['province'].isin(province)]
                if collegeName is not None and collegeName != '':
                    datadf = datadf[datadf['collegeName'].str.contains(collegeName)]
                #不输入分数，默认为2019年的
                if year is None or year == '':
                    # 默认为2019年数据
                    year = 2019
                datadf = datadf[datadf['year'] == int(year)]
                # 数据中有NAN，json不能转换，需要处理W为‘’
                datadf = datadf.fillna('')
                datadf = datadf.sort_values(by=['moveDocGrade'], ascending=False)
            else:
                datadf = pd.DataFrame(data)
                if sequence is not None and sequence != '':
                    datadf = datadf[datadf['sequence'] == sequence]
                if province is not None and province != '':
                    province = province.split(',')
                    datadf = datadf[datadf['province'].isin(province)]
                if collegeName is not None and collegeName != '':
                    datadf = datadf[datadf['collegeName'].str.contains(collegeName)]
                if year is None or year == '':
                    #默认为2019年数据
                    year = 2019
                datadf = datadf[datadf['year']== int(year)]
                datadf = datadf[datadf['moveDocGrade'] <= int(score)]
                datadf = datadf.sort_values(by=['moveDocGrade'], ascending=False)
                #数据中有NAN，json不能转换，需要处理W为‘’
                datadf = datadf.fillna('')
            data_list = []
            for index, data in datadf.iterrows():
                item = {'collegeCode': data['collegeCode'], 'collegeHistoryId': data['collegeHistoryId'],
                        'collegeName': data['collegeName'], 'province': data['province'],
                        'subject': data['subject'], 'sequence': data['sequence'],
                        'moveDocGrade': data['moveDocGrade'], 'averageGrade': data['averageGrade'],
                        'moveDocGradeDiff': data['moveDocGradeDiff'], 'averageGradeDiff': data['averageGradeDiff'],
                        'moveDocLocation': data['moveDocLocation'], 'averageLocation': data['averageLocation'],
                        'year': year}
                data_list.append(item)
            msg['code'] = 0
            msg['data'] = data_list
            return response.Response(msg)
        except:
            return response.Response(msg)
#查询单个理科学校的调档线  很多年的信息
class SciCollegeLineView(views.APIView):
    def get(self,request,pk):
        msg = {'code': 1, 'data': []}
        try:
            sciCollegeLine = SciCollegeLine.objects.filter(collegeHistoryId=pk,year__gt=2014).order_by('-year')
            serializer = SciCollegeLineAllSerializer(sciCollegeLine,many=True)
            msg['code'] = 0
            msg['data'] = serializer.data
            return response.Response(msg)
        except:
            return response.Response(msg)
#理科高校录取情况
class SciEnrollView(views.APIView):
    def get(self,request,pk):
        '''
        根据historycollgeid查询录取情况
        :param request:
        :param pk:
        :return:
        '''
        msg = {'code': 1, 'data': []}
        try:
            sciEnrolls = SciEnroll.objects.filter(collegeHistoryId=pk,historyProYear__gt=2014).order_by('-historyProYear')
            serializer = SciEnrollSerializer(sciEnrolls,many=True)
            msg['code'] = 0
            msg['data'] = serializer.data
            return response.Response(msg)
        except:
            return response.Response(msg)
#查询理科学校专业录取信息
class SciMajorLineView(views.APIView):
    def get(self,request,pk):
        '''
        根据collegehistoryid和year查询学校专业录取信息
        :param request:
        :param pk:
        :return:
        '''
        msg = {'code': 1, 'data': []}
        param = request.query_params.dict()
        year = param['year']
        try:
            sciMjorLines = SciMajorLine.objects.filter(collegeHistoryId=pk,year=year).all()
            serializers = SciMajorLineSerializer(sciMjorLines,many=True)
            msg['code'] = 0
            msg['data'] = serializers.data
            return response.Response(msg)
        except:
            return response.Response(msg)
    def post(self,request,*args,**kwargs):
        '''
        查询某个学校某个专业近几年的录取情况
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        msg = {'code':1,'data':[]}
        try:
            collegeHistoryId = request.data.get('collegeHistoryId')
            speicaltyName = request.data.get('speicaltyName')
            sciMajorLines = SciMajorLine.objects.filter(collegeHistoryId=collegeHistoryId,speicaltyName=speicaltyName,year__gt=2014)
            serializer = SciMajorLineSerializer(sciMajorLines,many=True)
            msg['code']=0
            msg['data'] = serializer.data
            return response.Response(msg)
        except:
            return response.Response(msg)
#文科调档线 这里返回部分数据，用于列表显示
class ArtsCollegeLineListView(views.APIView):
    def get(self,request):
        msg = {'code': 1, 'data': []}
        try:
            key = settings.REDIS_ALLARTSCOLLEGELINE
            data = cache.get(key)
            if data is None:
                ArtsCollegeLines = ArtsCollegeLine.objects.all()
                serializer = ArtsCollegeLineAllSerializer(ArtsCollegeLines,many=True)
                cache.set(key, serializer.data, settings.REDIS_TIMEOUT)
                datadf = pd.DataFrame(serializer.data)
            else:
                datadf = pd.DataFrame(data)
            # 默认为2019年数据
            datadf = datadf[datadf['year'] == 2019]
            datadf = datadf.sort_values(by=['moveDocGrade'], ascending=False)
            # 数据中有NAN，json不能转换，需要处理W为‘’
            datadf = datadf.fillna('')
            data_list = []
            for index, data in datadf.iterrows():
                item = {'collegeCode': data['collegeCode'], 'collegeHistoryId': data['collegeHistoryId'],
                            'collegeName': data['collegeName'], 'province': data['province'],
                            'subject': data['subject'], 'sequence': data['sequence'],
                            'moveDocGrade': data['moveDocGrade'], 'averageGrade': data['averageGrade'],'moveDocGradeDiff':data['moveDocGradeDiff'],'averageGradeDiff':data['averageGradeDiff'],
                            'moveDocLocation': data['moveDocLocation'], 'averageLocation': data['averageLocation'],
                            'year': '2019'}
                data_list.append(item)
            msg['code'] = 0
            msg['data'] = data_list
            # return response.Response('msg')
            return response.Response(msg)
        except:
            return response.Response(msg)
    def post(self,request):
        '''
        根据输入条件查询文科调档学校信息
        :param request:
        :return:
        '''
        msg = {'code': 1, 'data': []}
        try:
            province = request.data.get('province')
            collegeName = request.data.get('key')
            sequence = request.data.get('sequence')
            score = request.data.get('score')
            year = request.data.get('year')
            key = settings.REDIS_ALLARTSCOLLEGELINE
            data = cache.get(key)
            if score is None or score == '':
                if data is None:
                    return response.Response(msg)
                else:
                    datadf = pd.DataFrame(data)
                if sequence is not None and sequence != '':
                    datadf = datadf[datadf['sequence'] == sequence]
                if province is not None and province != '':
                    province = province.split(',')
                    datadf = datadf[datadf['province'].isin(province)]
                if collegeName is not None and collegeName != '':
                    datadf = datadf[datadf['collegeName'].str.contains(collegeName)]
                # 不输入分数，默认为2019年的
                if year is None or year == '':
                    # 默认为2019年数据
                    year = 2019
                datadf = datadf[datadf['year'] == int(year)]
                # 数据中有NAN，json不能转换，需要处理W为‘’
                datadf = datadf.fillna('')
                datadf = datadf.sort_values(by=['moveDocGrade'], ascending=False)
            else:
                if data is None:
                    return response.Response(msg)
                else:
                    datadf = pd.DataFrame(data)
                if sequence is not None and sequence != '':
                    datadf = datadf[datadf['sequence'] == sequence]
                if province is not None and province != '':
                    province = province.split(',')
                    datadf = datadf[datadf['province'].isin(province)]
                if collegeName is not None and collegeName != '':
                    datadf = datadf[datadf['collegeName'].str.contains(collegeName)]
                if year is None or year == '':
                    year = 2019
                datadf = datadf[datadf['year'] == int(year)]
                datadf = datadf[datadf['moveDocGrade'] <= int(score)]
                datadf = datadf.sort_values(by=['moveDocGrade'], ascending=False)
                # 数据中有NAN，json不能转换，需要处理W为‘’
                datadf = datadf.fillna('')
            data_list = []
            for index, data in datadf.iterrows():
                item = {'collegeCode': data['collegeCode'], 'collegeHistoryId': data['collegeHistoryId'],
                        'collegeName': data['collegeName'], 'province': data['province'],
                        'subject': data['subject'], 'sequence': data['sequence'],
                        'moveDocGrade': data['moveDocGrade'], 'averageGrade': data['averageGrade'],
                        'moveDocGradeDiff': data['moveDocGradeDiff'], 'averageGradeDiff': data['averageGradeDiff'],
                        'moveDocLocation': data['moveDocLocation'], 'averageLocation': data['averageLocation'],
                        'year': year}
                data_list.append(item)
            msg['code'] = 0
            msg['data'] = data_list
            return response.Response(msg)
        except:
            return response.Response(msg)
#查询单个文科学校的调档线 很多年的信息
class ArtsCollegeLineView(views.APIView):
    def get(self,request,pk):
        msg = {'code': 1, 'data': []}
        try:
            artsCollegeLine = ArtsCollegeLine.objects.filter(collegeHistoryId=pk,year__gt=2014).order_by('-year')
            serializer = ArtsCollegeLineAllSerializer(artsCollegeLine,many=True)
            msg['code'] = 0
            msg['data'] = serializer.data
            return response.Response(msg)
        except:
            return response.Response(msg)
#查询文科学校专业录取信息
class ArtsMajorLineView(views.APIView):
    def get(self,request,pk):
        '''
        根据collegehistoryid和year查询学校专业录取信息
        :param request:
        :param pk:
        :return:
        '''
        msg = {'code': 1, 'data': []}
        param = request.query_params.dict()
        year = param['year']
        try:
            artsMjorLines = ArtsMajorLine.objects.filter(collegeHistoryId=pk, year=year).all()
            serializers = ArtsMajorLineSerializer(artsMjorLines, many=True)
            msg['code'] = 0
            msg['data'] = serializers.data
            return response.Response(msg)
        except:
            return response.Response(msg)
    def post(self,request,*args,**kwargs):
        '''
        查询某个学校某个专业近几年的录取情况
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        msg = {'code':1,'data':[]}
        try:
            collegeHistoryId = request.data.get('collegeHistoryId')
            speicaltyName = request.data.get('speicaltyName')
            artsMajorLines = ArtsMajorLine.objects.filter(collegeHistoryId=collegeHistoryId,speicaltyName=speicaltyName,year__gt=2014)
            serializer = SciMajorLineSerializer(artsMajorLines,many=True)
            msg['code']=0
            msg['data'] = serializer.data
            return response.Response(msg)
        except:
            return response.Response(msg)
#文科高校录取情况
class ArtsEnrollView(views.APIView):
    def get(self,request,pk):
        '''
        根据historycollgeid查询录取情况
        :param request:
        :param pk:
        :return:
        '''
        msg = {'code': 1, 'data': []}
        try:
            artsEnrolls = ArtsEnroll.objects.filter(collegeHistoryId=pk,historyProYear__gt=2014).order_by('-historyProYear')
            serializer = SciEnrollSerializer(artsEnrolls, many=True)
            msg['code'] = 0
            msg['data'] = serializer.data
            return response.Response(msg)
        except:
            return response.Response(msg)
#批次
class OrderListView(views.APIView):
    def get(self,request):
        msg = {'code': 1,'options':[]}
        try:
            #先查所有节点
            orders = Order.objects.all()
            serializer = OrderAllSerializer(orders,many=True)
            #获取到所有的数据
            datas = serializer.data
            #将queryset转换为list，以便后续操作
            list_datas = []
            for data in datas:
                item = {'id':data['id'],'name':data['name'],'parentId':data['parentId']}
                list_datas.append(item)
            #定义一个和list_datas 一样的列表
            new_datas =[]
            #s输出列表
            d_datas =[]
            for list_data in list_datas:
                #每列都添加一个 children
                list_data['children'] = []
                #list_datas = new_datas
                new_datas.append(list_data)
            children_id = []
            for list_data in list_datas:
                for new_data in new_datas:
                    if list_data['id'] == new_data['parentId']:
                        list_data['children'].append(new_data)
                        children_id.append(new_data['id'])
                if list_data['id'] not in children_id:
                    d_datas.append(list_data)

            msg['code'] = 0
            msg['options'] = d_datas
            return response.Response(msg)
        except:
            return response.Response(msg)
#省
class ProvinceView(views.APIView):
    def get(self, request):
        msg = {'code': 1, 'data': []}
        try:
            provinces = Province.objects.all()
            serializer = ProvinceSerializer(provinces,many=True)
            msg['code'] = 0
            msg['data'] = serializer.data
            return response.Response(msg)
        except:
            return response.Response(msg)
#登录认证
class Login(views.APIView):
    def post(self,request,*args,**kwargs):
        '''
        用户登录认证
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        msg = {'code': 1}
        try:
            #用get方法取，不存在即为null
            userName = request.data.get("user")
            pwd = request.data.get("pwd")
            pwd = md5.password_md5(pwd)
            user = User.objects.filter(userName=userName,password=pwd).first()
            if not user:
                msg['error'] = "用户名或者密码错误"
            else:
                msg['code'] = 0
                uid = str(uuid.uuid4())  # 将生成的随机对象转化为随机字符串
                UserToken.objects.update_or_create(userName=user,defaults={"token":uid})
                msg['token'] = uid
            return response.Response(msg)
        except:
            msg['error'] = "系统错误"
            return response.Response(msg)
#预测学校
class ForecastCollegeView(views.APIView):
    def post(self,request,*args,**kwargs):
        msg = {'code':1}
        try:
            score = request.data.get("score")
            score = int(score)
            rate = request.data.get("rate")
            rate = int(rate)
            mark = request.data.get("mark")
            subject = request.data.get("subject")
            order = request.data.get("order")
            province = request.data.get("province")
            if score is None or score == '':
                return response.Response({'code': 0, 'data': []})
            if mark is None or mark =='':
                return response.Response({'code': 0, 'data': []})
            if rate is None or rate =='':
                return response.Response({'code': 0, 'data': []})
            if subject == '理科':
                datas,low_rank = forecast_sciuniverity(score,mark,rate)
            elif subject == '文科':
                datas,low_rank = forecast_artuniverity(score,mark,rate)
            else:
                return response.Response({'code':0,'data':[]})
            #进行省份和批次的过滤
            if order is not None and order != '':
                datas = datas[datas['sequence'] == order]
            if province is not None and province != '':
                province = province.split(',')
                # pass
                datas = datas[datas['province'].isin(province)]
            #将dataframe转换成list的map格式，方便返回json
            data_list = []
            for index,data in datas.iterrows():
                item = {'collegeCode':data['collegeCode'],'collegeHistoryId':data['collegeHistoryId'],
                        'province':data['province'],'collegeName':data['collegeName'],'subject':data['subject'],
                        'sequence':data['sequence'],'forecast_score':data['forecast_score'],'plan':data['plan']}
                data_list.append(item)
            return response.Response({"code":0,"data":data_list,"low_rank":low_rank})
        except:
            msg['error'] = "系统错误"
            return response.Response(msg)
#预测专业
class ForecastMajorView(views.APIView):
    def post(self,request,*args,**kwargs):
        try:
            collegeCode = request.data.get('collegeCode')
            collegeHistoryId = request.data.get('collegeHistoryId')
            low_rank = request.data.get('low_rank')
            subject = request.data.get("subject")
            if subject == '理科':
                datas = forecast_scimajor(collegeCode,collegeHistoryId,low_rank)
            else:
                datas = forecast_artsmajor(collegeCode,collegeHistoryId,low_rank)
            #将dataframe转换成list的map格式，方便返回json
            data_list = []
            for index,data in datas.iterrows():
                item = {'collegeCode':data['collegeCode'],'collegeHistoryId':data['collegeHistoryId'],
                        'collegeName':data['collegeName'],'sequence':data['sequence'],'speicaltyName':data['speicaltyName'],
                        'code':data['code'],'score':data['forecast_score']}
                data_list.append(item)
            return response.Response({"code":0,"data":data_list})
        except:
            return response.Response({'code':1,"error":'系统错误'})
#专业实力
class MajorAbilityView(views.APIView):
    def get(self,request,pk,*args,**kwargs):
        '''
        根据学校id查询专业实力
        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        '''
        msg = {'code':1,'data':[]}
        try:
            majorAbilities = MajorAbility.objects.filter(collegeCode=pk).all()
            serializer = MajorAbilitySerializer(majorAbilities,many=True)
            msg['code'] = 0
            msg['data'] = serializer.data
            return response.Response(msg)
        except:
            return response.Response(msg)
#招生简章
class EnrollmentGuldeView(views.APIView):
    def get(self,request,pk):
        '''
        根据collgeCode查询招生简章
        :param request:
        :param pk:
        :return:
        '''
        msg = {'code':1,'data':[]}
        try:
            enrollmentGuldes = EnrollmentGulde.objects.filter(collegeCode=pk).all()
            serializers = EnrollmentGuldeSerializer(enrollmentGuldes,many=True)
            msg['code'] = 0
            msg['data'] = serializers.data
            return response.Response(msg)
        except:
            return response.Response(msg)
#专业库的一级菜单
class OneMajorInfoView(views.APIView):
    def post(self,request):
        msg = {'code':1,'data':[]}
        try:
            specialtyLevelName = request.data.get('specialtyLevelName')
            sql = "SELECT * FROM web_majorinfo WHERE specialtyLevelName='{}'GROUP BY parentCategoryName ORDER BY id ASC".format(specialtyLevelName)
            oneMajorInfos = MajorInfo.objects.raw(sql)
            serializers = MajorInfoSerializer(oneMajorInfos,many=True)
            msg['code'] = 0
            msg['data'] = serializers.data
            return response.Response(msg)
        except:
            return  response.Response(msg)
#专业库的二级菜单
class TwoMajorInfoView(views.APIView):
    def post(self,request):
        msg = {'code':1,'data':[]}
        try:
            specialtyLevelName = request.data.get('specialtyLevelName')
            parentCategoryName = request.data.get('parentCategoryName')
            sql = "SELECT * FROM web_majorinfo WHERE specialtyLevelName='{}' AND parentCategoryName='{}' GROUP BY categoryName ORDER BY id ASC".format(specialtyLevelName,parentCategoryName)
            twoMajorInfos = MajorInfo.objects.raw(sql)
            serializers = MajorInfoSerializer(twoMajorInfos,many=True)
            msg['code'] = 0
            msg['data'] = serializers.data
            return response.Response(msg)
        except:
            return  response.Response(msg)
#专业库的三级菜单
class ThreeMajorInfoView(views.APIView):
    def post(self,request):
        msg = {'code':1,'data':[]}
        try:
            specialtyLevelName = request.data.get('specialtyLevelName')
            parentCategoryName = request.data.get('parentCategoryName')
            categoryName = request.data.get('categoryName')
            sql = "SELECT * FROM web_majorinfo WHERE specialtyLevelName='{}' AND parentCategoryName='{}' AND categoryName='{}' ORDER BY id ASC;".format(specialtyLevelName,parentCategoryName,categoryName)
            threeMajorInfos = MajorInfo.objects.raw(sql)
            serializers = MajorInfoSerializer(threeMajorInfos,many=True)
            msg['code'] = 0
            msg['data'] = serializers.data
            return response.Response(msg)
        except:
            return  response.Response(msg)
#点击专业查询开设的学校
class Major2CollegeView(views.APIView):
    def post(self,request):
        msg = {'code':1,'data':[]}
        try:
            specialtyLevelName = request.data.get('specialtyLevelName')
            speicaltyName = request.data.get('speicaltyName')
            order_list = ['A+', 'A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'E+', 'E', 'F+', 'F', '']
            ordering = 'FIELD(`specialtyComment`, {})'.format(','.join([ "'{}'".format(i) for i in order_list]))
            majorAbilities = MajorAbility.objects.filter(specialtyLevelName=specialtyLevelName,speicaltyName=speicaltyName).extra(select={'ordering': ordering}, order_by=('ordering','specialtyPlace'))
            serializers = MajorAbilitySerializer(majorAbilities,many=True)
            msg['code'] = 0
            msg['data'] = serializers.data
            return response.Response(msg)
        except:
            return response.Response(msg)
#根据条件查询专业
class MajorView(views.APIView):
    def post(self,request):
        msg = {'code':1,'data':0}
        try:
            specialtyLevelName = request.data.get('specialtyLevelName')
            key = request.data.get('key')
            majorInfos = MajorInfo.objects.filter(specialtyLevelName=specialtyLevelName,speicaltyName__icontains=key).all()
            serializers = MajorInfoSerializer(majorInfos,many=True)
            msg['code'] = 0
            msg['data'] = serializers.data
            return response.Response(msg)
        except:
            return response.Response(msg)




