from django.db import models




#理科专业分数线
class SciMajorLine(models.Model):
    collegeCode = models.IntegerField('学校编码',max_length=8)
    collegeHistoryId = models.IntegerField(max_length=8)
    province = models.CharField('省份',max_length=16)
    collegeName = models.CharField('学校名称',max_length=100)
    subject = models.CharField('类别',max_length=8)
    sequence = models.CharField('批次',max_length=100)
    year = models.IntegerField('年',max_length=5)
    speicaltyName = models.CharField('专业名称',max_length=130)
    matricGrade = models.IntegerField('实录分数',max_length=5)
    specialtyGradeDiff = models.IntegerField('本一实录线差',max_length=5)
    matricGradePosition = models.IntegerField('本一实录位次',max_length=10)
    positionMatricGrade = models.IntegerField('成都二诊同位实录分',max_length=5)
    averageGrade = models.IntegerField('平均分数',max_length=5)
    averageGradeDiff = models.IntegerField('本一平均线差',max_length=5)
    averageGradePosition = models.IntegerField('本一平均位次',max_length=10)
    positionAverageGrade = models.IntegerField('成都二诊同位平均分',max_length=5)

    # def matricGradePosition1(self):
    #     if self.matricGradePosition == -999999999:
    #         return '——'
    #     else:
    #         return self.matricGradePosition

    class Meta:
        ordering=('collegeCode',)

    # matricGradePosition1.short_description = '本一实录位次'
#文科专业线
class ArtsMajorLine(models.Model):
    collegeCode = models.IntegerField('学校编码',max_length=8)
    collegeHistoryId = models.IntegerField(max_length=8)
    province = models.CharField('省份',max_length=16)
    collegeName = models.CharField('学校名称',max_length=100)
    subject = models.CharField('类别',max_length=8)
    sequence = models.CharField('批次',max_length=100)
    year = models.IntegerField('年',max_length=5)
    speicaltyName = models.CharField('专业名称',max_length=130)
    matricGrade = models.IntegerField('实录分数',max_length=5)
    specialtyGradeDiff = models.IntegerField('本一实录线差',max_length=5)
    matricGradePosition = models.IntegerField('本一实录位次',max_length=10)
    positionMatricGrade = models.IntegerField('成都二诊同位实录分',max_length=5)
    averageGrade = models.IntegerField('平均分数',max_length=5)
    averageGradeDiff = models.IntegerField('本一平均线差',max_length=5)
    averageGradePosition = models.IntegerField('本一平均位次',max_length=10)
    positionAverageGrade = models.IntegerField('成都二诊同位平均分',max_length=5)

    class Meta:
        ordering=('collegeCode',)

#文科调档线
class ArtsCollegeLine(models.Model):
    collegeCode = models.IntegerField('学校编码', max_length=8)
    collegeHistoryId = models.IntegerField(max_length=8)
    province = models.CharField('省份', max_length=16)
    collegeName = models.CharField('学校名称', max_length=100)
    subject = models.CharField('类别', max_length=8)
    sequence = models.CharField('批次', max_length=100)
    year = models.IntegerField('年', max_length=5)
    moveDocGrade = models.IntegerField('调档分',max_length=5)
    averageGrade = models.IntegerField('平均分',max_length=5)
    moveDocGradeDiff = models.IntegerField('调档本一线差',max_length=5)
    averageGradeDiff = models.IntegerField('平均本一线差',max_length=5)
    moveDocLocation = models.IntegerField('调档分位次',max_length=10)
    positionMoveDocGrade = models.IntegerField('成都二诊同位调档分',max_length=5)
    averageLocation = models.IntegerField('平均分位次',max_length=10)
    positionAverageGrade = models.IntegerField('成都二诊同位平均分',max_length=5)

    class Meta:
        ordering = ('collegeCode',)

#理科调档线
class SciCollegeLine(models.Model):
    collegeCode = models.IntegerField('学校编码', max_length=8)
    collegeHistoryId = models.IntegerField(max_length=8)
    province = models.CharField('省份', max_length=16)
    collegeName = models.CharField('学校名称', max_length=100)
    subject = models.CharField('类别', max_length=8)
    sequence = models.CharField('批次', max_length=100)
    year = models.IntegerField('年', max_length=5)
    moveDocGrade = models.IntegerField('调档分',max_length=5)
    averageGrade = models.IntegerField('平均分',max_length=5)
    moveDocGradeDiff = models.IntegerField('调档本一线差',max_length=5)
    averageGradeDiff = models.IntegerField('平均本一线差',max_length=5)
    moveDocLocation = models.IntegerField('调档分位次',max_length=10)
    positionMoveDocGrade = models.IntegerField('成都二诊同位调档分',max_length=5)
    averageLocation = models.IntegerField('平均分位次',max_length=10)
    positionAverageGrade = models.IntegerField('成都二诊同位平均分',max_length=5)

    class Meta:
        ordering = ('collegeCode',)

#专业实力
class MajorAbility(models.Model):
    collegeCode = models.IntegerField('学校编码', max_length=8)
    specialtyCode = models.IntegerField('专业编码',max_length=10)
    speicaltyName = models.CharField('专业名称',max_length=130)
    specialtyPlace = models.IntegerField('专业名次',max_length=5)
    specialtyComment = models.CharField('专业级别',max_length=5)
    collegeCount = models.IntegerField('开设院校数',max_length=6)
    isKeyConstruction = models.BooleanField('国家特色专业')
    def collegeName(self):
        collegeInfo = CollegeInfo.objects.filter(collegeCode=self.collegeCode).first()
        return collegeInfo.collegeName
    collegeName.short_description='学校名称'
    class Meta:
        ordering = ('collegeCode',)

#学校信息
class CollegeInfo(models.Model):
    collegeCode = models.AutoField('学校编码',primary_key=True)
    collegeName = models.CharField('学校名称',max_length=100)
    categoryName = models.CharField('类型',max_length=5)
    propertyName = models.CharField('性质',max_length=8)
    levelName = models.CharField('级别',max_length=100)
    provinceName = models.CharField('省份',max_length=16)
    cityName = models.CharField('城市',max_length=16)
    address = models.CharField('地址',max_length=150)
    url = models.CharField('学校官网',max_length=100)
    phone = models.CharField('招生电话',max_length=100)
    introduce = models.TextField('学校简介')
    class Meta:
        ordering = ('collegeCode',)

#理科高校录取情况
class SciEnroll(models.Model):
    collegeCode = models.IntegerField('学校编码',max_length=6)
    collegeHistoryId =models.IntegerField(max_length=6)
    province = models.CharField('省份',max_length=16)
    collegeName = models.CharField('学校名称',max_length=100)
    subject = models.CharField('类别',max_length=8)
    sequence = models.CharField('批次',max_length=100)
    historyProYear = models.IntegerField('年',max_length=5)
    realRecruitTotal = models.IntegerField('实际招生人数',max_length=7)
    firstWishTotal = models.IntegerField('批线上第一 志愿报考数',max_length=8)
    enrollProperty = models.CharField('录取性质',max_length=7)
    firstWishSucTotal = models.IntegerField('第一志愿录取数',max_length=7)
    secondWishSucTotal =  models.IntegerField('其他志愿录取数',max_length=7)
    class Meta:
        ordering = ('collegeCode',)

#文科高校录取情况
class ArtsEnroll(models.Model):
    collegeCode = models.IntegerField('学校编码',max_length=6)
    collegeHistoryId =models.IntegerField(max_length=6)
    province = models.CharField('省份',max_length=16)
    collegeName = models.CharField('学校名称',max_length=100)
    subject = models.CharField('类别',max_length=8)
    sequence = models.CharField('批次',max_length=100)
    historyProYear = models.IntegerField('年',max_length=5)
    realRecruitTotal = models.IntegerField('实际招生人数',max_length=7)
    firstWishTotal = models.IntegerField('批线上第一 志愿报考数',max_length=8)
    enrollProperty = models.CharField('录取性质',max_length=7)
    firstWishSucTotal = models.IntegerField('第一志愿录取数',max_length=7)
    secondWishSucTotal =  models.IntegerField('其他志愿录取数',max_length=7)
    class Meta:
        ordering = ('collegeCode',)

