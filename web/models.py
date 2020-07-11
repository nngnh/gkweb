from django.db import models
from django.contrib.auth.hashers import make_password
from web.utils import md5

#理科专业分数线
class SciMajorLine(models.Model):
    collegeCode = models.IntegerField('学校编码',blank=True,null=True)
    collegeHistoryId = models.IntegerField(blank=True,null=True)
    province = models.CharField('省份',max_length=16,blank=True,null=True)
    collegeName = models.CharField('学校名称',max_length=100,blank=True,null=True)
    subject = models.CharField('类别',max_length=8,blank=True,null=True)
    sequence = models.CharField('批次',max_length=100,blank=True,null=True)
    year = models.IntegerField('年',blank=True,null=True)
    speicaltyName = models.CharField('专业名称',max_length=130,blank=True,null=True)
    matricGrade = models.IntegerField('实录分数',blank=True,null=True)
    specialtyGradeDiff = models.IntegerField('本一实录线差',blank=True,null=True)
    matricGradePosition = models.IntegerField('本一实录位次',blank=True,null=True)
    positionMatricGrade = models.IntegerField('成都二诊同位实录分',blank=True,null=True)
    averageGrade = models.IntegerField('平均分数',blank=True,null=True)
    averageGradeDiff = models.IntegerField('本一平均线差',blank=True,null=True)
    averageGradePosition = models.IntegerField('本一平均位次',blank=True,null=True)
    positionAverageGrade = models.IntegerField('成都二诊同位平均分',blank=True,null=True)

    class Meta:
        ordering=('collegeCode',)
        verbose_name = u'理科专业录取线'
        verbose_name_plural = verbose_name  # 表示复数
#文科专业线
class ArtsMajorLine(models.Model):
    collegeCode = models.IntegerField('学校编码',blank=True,null=True)
    collegeHistoryId = models.IntegerField(blank=True,null=True)
    province = models.CharField('省份',max_length=16,blank=True,null=True)
    collegeName = models.CharField('学校名称',max_length=100,blank=True,null=True)
    subject = models.CharField('类别',max_length=8,blank=True,null=True)
    sequence = models.CharField('批次',max_length=100,blank=True,null=True)
    year = models.IntegerField('年',blank=True,null=True)
    speicaltyName = models.CharField('专业名称',max_length=130,blank=True,null=True)
    matricGrade = models.IntegerField('实录分数',blank=True,null=True)
    specialtyGradeDiff = models.IntegerField('本一实录线差',blank=True,null=True)
    matricGradePosition = models.IntegerField('本一实录位次',blank=True,null=True)
    positionMatricGrade = models.IntegerField('成都二诊同位实录分',blank=True,null=True)
    averageGrade = models.IntegerField('平均分数',blank=True,null=True)
    averageGradeDiff = models.IntegerField('本一平均线差',blank=True,null=True)
    averageGradePosition = models.IntegerField('本一平均位次',blank=True,null=True)
    positionAverageGrade = models.IntegerField('成都二诊同位平均分',blank=True,null=True)

    class Meta:
        ordering=('collegeCode',)
        verbose_name = u'文科专业录取线'
        verbose_name_plural = verbose_name  # 表示复数
#文科调档线
class ArtsCollegeLine(models.Model):
    collegeCode = models.IntegerField('学校编码',blank=True,null=True)
    collegeHistoryId = models.IntegerField(blank=True,null=True)
    province = models.CharField('省份', max_length=16,blank=True,null=True)
    collegeName = models.CharField('学校名称', max_length=100,blank=True,null=True)
    subject = models.CharField('类别', max_length=8,blank=True,null=True)
    sequence = models.CharField('批次', max_length=100,blank=True,null=True)
    year = models.IntegerField('年',blank=True,null=True)
    moveDocGrade = models.IntegerField('调档分',blank=True,null=True)
    averageGrade = models.IntegerField('平均分',blank=True,null=True)
    moveDocGradeDiff = models.IntegerField('调档本一线差',blank=True,null=True)
    averageGradeDiff = models.IntegerField('平均本一线差',blank=True,null=True)
    moveDocLocation = models.IntegerField('调档分位次',blank=True,null=True)
    positionMoveDocGrade = models.IntegerField('成都二诊同位调档分',blank=True,null=True)
    averageLocation = models.IntegerField('平均分位次',blank=True,null=True)
    positionAverageGrade = models.IntegerField('成都二诊同位平均分',blank=True,null=True)

    class Meta:
        ordering = ('collegeCode',)
        verbose_name = u'文科调档线'
        verbose_name_plural = verbose_name  # 表示复数
#理科调档线
class SciCollegeLine(models.Model):
    collegeCode = models.IntegerField('学校编码',blank=True,null=True)
    collegeHistoryId = models.IntegerField(blank=True,null=True)
    province = models.CharField('省份', max_length=16,blank=True,null=True)
    collegeName = models.CharField('学校名称', max_length=100,blank=True,null=True)
    subject = models.CharField('类别', max_length=8,blank=True,null=True)
    sequence = models.CharField('批次', max_length=100,blank=True,null=True)
    year = models.IntegerField('年', blank=True,null=True)
    moveDocGrade = models.IntegerField('调档分',blank=True,null=True)
    averageGrade = models.IntegerField('平均分',blank=True,null=True)
    moveDocGradeDiff = models.IntegerField('调档本一线差',blank=True,null=True)
    averageGradeDiff = models.IntegerField('平均本一线差',blank=True,null=True)
    moveDocLocation = models.IntegerField('调档分位次',blank=True,null=True)
    positionMoveDocGrade = models.IntegerField('成都二诊同位调档分',blank=True,null=True)
    averageLocation = models.IntegerField('平均分位次',blank=True,null=True)
    positionAverageGrade = models.IntegerField('成都二诊同位平均分',blank=True,null=True)

    class Meta:
        ordering = ('collegeCode',)
        '''
        后台显示的中文名
        '''
        verbose_name = u'理科调档线'
        verbose_name_plural = verbose_name  # 表示复数
#专业实力
class MajorAbility(models.Model):
    collegeCode = models.IntegerField('学校编码', blank=True,null=True)
    collegeName = models.CharField('学校名称',max_length=32,blank=True,null=True)
    specialtyCode = models.IntegerField('专业编码',blank=True,null=True)
    speicaltyName = models.CharField('专业名称',max_length=130,blank=True,null=True)
    specialtyPlace = models.IntegerField('专业名次',blank=True,null=True)
    specialtyComment = models.CharField('专业级别',max_length=5,blank=True,null=True)
    collegeCount = models.IntegerField('开设院校数',blank=True,null=True)
    isKeyConstruction = models.BooleanField('国家特色专业')
    specialtyLevelName = models.CharField('本/专',max_length=4,blank=True,null=True)
    class Meta:
        ordering = ('collegeCode',)
        verbose_name = u'专业实力'
        verbose_name_plural = verbose_name  # 表示复数
#学校信息
class CollegeInfo(models.Model):
    collegeCode = models.IntegerField('学校编码',blank=True,null=True)
    collegeName = models.CharField('学校名称',max_length=100,blank=True,null=True)
    categoryName = models.CharField('类型',max_length=5,blank=True,null=True)
    propertyName = models.CharField('性质',max_length=8,blank=True,null=True)
    levelName = models.CharField('级别',max_length=100,blank=True,null=True)
    provinceName = models.CharField('省份',max_length=16,blank=True,null=True)
    cityName = models.CharField('城市',max_length=16,blank=True,null=True)
    address = models.CharField('地址',max_length=150,blank=True,null=True)
    url = models.CharField('学校官网',max_length=100,blank=True,null=True)
    phone = models.CharField('招生电话',max_length=100,blank=True,null=True)
    introduce = models.TextField('学校简介',null=True)
    class Meta:
        ordering = ('collegeCode',)
        verbose_name = u'学校信息'
        verbose_name_plural = verbose_name  # 表示复数

    def profile(self):
        if len(self.introduce) > 60:
            return '{}........'.format(self.introduce[0:59])
        else:
            return self.introduce
    profile.allow_tags = True
#理科高校录取情况
class SciEnroll(models.Model):
    collegeCode = models.IntegerField('学校编码',blank=True,null=True)
    collegeHistoryId =models.IntegerField(blank=True,null=True)
    province = models.CharField('省份',max_length=16,blank=True,null=True)
    collegeName = models.CharField('学校名称',max_length=100,blank=True,null=True)
    subject = models.CharField('类别',max_length=32,blank=True,null=True)
    sequence = models.CharField('批次',max_length=100,blank=True,null=True)
    historyProYear = models.IntegerField('年',blank=True,null=True)
    realRecruitTotal = models.IntegerField('实际招生人数',blank=True,null=True)
    firstWishTotal = models.IntegerField('批线上第一 志愿报考数',blank=True,null=True)
    enrollProperty = models.CharField('录取性质',max_length=7,blank=True,null=True)
    firstWishSucTotal = models.IntegerField('第一志愿录取数',blank=True,null=True)
    secondWishSucTotal =  models.IntegerField('其他志愿录取数',blank=True,null=True)
    class Meta:
        ordering = ('collegeCode',)
        verbose_name = u'理科高校录取情况'
        verbose_name_plural = verbose_name  # 表示复数
#文科高校录取情况
class ArtsEnroll(models.Model):
    collegeCode = models.IntegerField('学校编码',blank=True,null=True)
    collegeHistoryId =models.IntegerField(blank=True,null=True)
    province = models.CharField('省份',max_length=16,blank=True,null=True)
    collegeName = models.CharField('学校名称',max_length=100,blank=True,null=True)
    subject = models.CharField('类别',max_length=32,blank=True,null=True)
    sequence = models.CharField('批次',max_length=100,blank=True,null=True)
    historyProYear = models.IntegerField('年',blank=True,null=True)
    realRecruitTotal = models.IntegerField('实际招生人数',blank=True,null=True)
    firstWishTotal = models.IntegerField('批线上第一 志愿报考数',blank=True,null=True)
    enrollProperty = models.CharField('录取性质',max_length=7,blank=True,null=True)
    firstWishSucTotal = models.IntegerField('第一志愿录取数',blank=True,null=True)
    secondWishSucTotal =  models.IntegerField('其他志愿录取数',blank=True,null=True)
    class Meta:
        ordering = ('collegeCode',)
        verbose_name = u'文科高校录取情况'
        verbose_name_plural = verbose_name  # 表示复数
#理科学校的一分一段表
class SciYiFenYiDuan(models.Model):
    province = models.CharField('省份',max_length=16,blank=True,null=True)
    year = models.IntegerField('年',blank=True,null=True)
    subject = models.CharField('类别',max_length=8,blank=True,null=True)
    score = models.IntegerField('分数',blank=True,null=True)
    num = models.IntegerField('人数',blank=True,null=True)
    rank = models.IntegerField('排名',blank=True,null=True)
    class Meta:
        ordering = ('-score',)
        verbose_name = u'理科一分一段'
        verbose_name_plural = verbose_name  # 表示复数
#文科学校的一分一段表
class ArtYiFenYiDuan(models.Model):
    province = models.CharField('省份',max_length=16,blank=True,null=True)
    year = models.IntegerField('年',blank=True,null=True)
    subject = models.CharField('类别',max_length=8,blank=True,null=True)
    score = models.IntegerField('分数',blank=True,null=True)
    num = models.IntegerField('人数',blank=True,null=True)
    rank = models.IntegerField('排名',blank=True,null=True)
    class Meta:
        ordering = ('-score',)
        verbose_name = u'文科一分一段'
        verbose_name_plural = verbose_name  # 表示复数

#学校批次
class Order(models.Model):
    name = models.CharField('名称',max_length=64)
    parentId = models.IntegerField('父节点')
    class Meta:
        ordering = ('id',)
        verbose_name = u'录取批次'
        verbose_name_plural = verbose_name  # 表示复数

#用户
class User(models.Model):
    userName = models.CharField('用户名',max_length=32)
    password = models.CharField('密码',max_length=128)
    def save(self,*args,**kwargs):
        self.password = md5.password_md5(self.password)
        super(User,self).save(*args,**kwargs)

    class Meta:
        ordering = ('id',)
        verbose_name = u'用户'
        verbose_name_plural = verbose_name  # 表示复数
#保存用户登录的token
class UserToken(models.Model):
    userName = models.OneToOneField(to="User",on_delete=models.CASCADE)
    token = models.CharField(max_length=64)
#省份
class Province(models.Model):
    provinceName = models.CharField('名称',max_length=8)
    class Meta:
        verbose_name = u'省份'
        verbose_name_plural = verbose_name  # 表示复数

#理科录取计划
class SciPlan(models.Model):
    collegeName = models.CharField('学校名称',max_length=32,blank=True,null=True)
    province = models.CharField('省份',max_length=8,blank=True,null=True)
    code = models.IntegerField('招生代码',blank=True,null=True)
    subject = models.CharField('科类',max_length=8,blank=True,null=True)
    sequence = models.CharField('批次',max_length=32,blank=True,null=True)
    plan = models.IntegerField('计划数',blank=True,null=True)
    isAdd = models.BooleanField('是否新增',blank=True,null=True)
    year = models.IntegerField('年',blank=True,null=True)
    class Meta:
        verbose_name = u'招生计划'
        verbose_name_plural = verbose_name  # 表示复数
#文科录取计划
class ArtsPlan(models.Model):
    collegeName = models.CharField('学校名称',max_length=32,blank=True,null=True)
    province = models.CharField('省份',max_length=8,blank=True,null=True)
    code = models.IntegerField('招生代码',blank=True,null=True)
    subject = models.CharField('科类',max_length=8,blank=True,null=True)
    sequence = models.CharField('批次',max_length=32,blank=True,null=True)
    plan = models.IntegerField('计划数',blank=True,null=True)
    isAdd = models.BooleanField('是否新增',blank=True,null=True)
    year = models.IntegerField('年',blank=True,null=True)
    class Meta:
        verbose_name = u'招生计划'
        verbose_name_plural = verbose_name  # 表示复数
#招生简章
class EnrollmentGulde(models.Model):
    collegeCode = models.IntegerField('学校编码')
    title = models.CharField('标题',max_length=64,blank=True,null=True)
    content = models.TextField('内容',null=True,blank=True)
    class Meta:
        ordering = ('collegeCode',)
        verbose_name = u'招生简章'
        verbose_name_plural = verbose_name  # 表示复数

    def EnrollmentGulde(self):
        if len(self.content) > 60:
            return '{}........'.format(self.content[0:59])
        else:
            return self.content
    EnrollmentGulde.allow_tags = True
#专业库
class MajorInfo(models.Model):
    speicaltyName = models.CharField('专业名称',max_length=32,blank=True,null=True)
    categoryName = models.CharField('类别',max_length=16)
    parentCategoryName = models.CharField('父级类别',max_length=16)
    graduateScale = models.CharField('毕业生规模',max_length=16,blank=True,null=True)
    employInterval = models.CharField('就业区间',max_length=4,blank=True,null=True)
    specialtyLevelName = models.CharField('本/专',max_length=2,blank=True,null=True)
    class Meta:
        verbose_name = u'专业库'
        verbose_name_plural = verbose_name  # 表示复数