from django.contrib import admin
from web.models import  *
from import_export import  resources
from import_export.admin import ImportExportModelAdmin,ImportExportActionModelAdmin

admin.site.site_header = '高考数据管理系统'
admin.site.site_title = '高考数据管理系统'
admin.site.index_title = u'高考数据管理系统'

#用于理科专业分数线的导入导出
class SciMajorLineResource(resources.ModelResource):
    class Meta:
        model = SciMajorLine
#理科专业分数线
class SciMajorLineAdmin(ImportExportActionModelAdmin):
    #显示需要显示的字段
    list_display = ['collegeCode','province','collegeName','subject','sequence','year','speicaltyName',
                    'matricGrade','specialtyGradeDiff','matricGradePosition','positionMatricGrade',
                    'averageGrade','averageGradeDiff','averageGradePosition','positionAverageGrade']
    actions_on_top = True
    list_per_page = 15
    list_filter = ('collegeName', 'speicaltyName',)
    # search_fields = ['collegeName','speicaltyName']
    #禁用修改
    readonly_fields = [field.name for field in SciMajorLine._meta.fields]
    def has_add_permission(self, request):
        # 禁用添加按钮
        return False
    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return False
admin.site.register(SciMajorLine,SciMajorLineAdmin)
#用于理科专业分数线的导入导出
class ArtsMajorLineResource(resources.ModelResource):
    class Meta:
        model = ArtsMajorLine
#文科专业分数线
class ArtsMajorLineAdmin(ImportExportActionModelAdmin):
    #显示需要显示的字段
    list_display = ['collegeCode','province','collegeName','subject','sequence','year','speicaltyName',
                    'matricGrade','specialtyGradeDiff','matricGradePosition','positionMatricGrade',
                    'averageGrade','averageGradeDiff','averageGradePosition','positionAverageGrade']
    actions_on_top = True
    list_per_page = 15
    list_filter = ('collegeName', 'speicaltyName',)
    # search_fields = ['collegeName','speicaltyName']
    #禁用修改
    readonly_fields = [field.name for field in ArtsMajorLine._meta.fields]
    def has_add_permission(self, request):
        # 禁用添加按钮
        return False
    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return False
admin.site.register(ArtsMajorLine,ArtsMajorLineAdmin)
#用于理科调档线的导入导出
class SciCollegeLineResource(resources.ModelResource):
    class Meta:
        model = SciMajorLine
#理科调档线
class SciCollegeLineAdmin(ImportExportActionModelAdmin):
    #显示需要显示的字段
    list_display = ['collegeCode','province','collegeName','subject','sequence','year','moveDocGrade',
                    'averageGrade','moveDocGradeDiff','averageGradeDiff','moveDocLocation',
                    'positionMoveDocGrade','averageLocation','positionAverageGrade']
    actions_on_top = True
    list_per_page = 15
    # list_filter = ('collegeName', 'speicaltyName',)
    #禁用修改
    readonly_fields = [field.name for field in SciCollegeLine._meta.fields]
    search_fields = ['collegeName']
    def has_add_permission(self, request):
        # 禁用添加按钮
        return False
    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return False
admin.site.register(SciCollegeLine,SciCollegeLineAdmin)\
#用于文科调档线的导入导出
class ArtsCollegeLineResource(resources.ModelResource):
    class Meta:
        model = ArtsCollegeLine
#文科调档线
class ArtsCollegeLineAdmin(ImportExportActionModelAdmin):
    #显示需要显示的字段
    list_display = ['collegeCode','province','collegeName','subject','sequence','year','moveDocGrade',
                    'averageGrade','moveDocGradeDiff','averageGradeDiff','moveDocLocation',
                    'positionMoveDocGrade','averageLocation','positionAverageGrade']
    actions_on_top = True
    list_per_page = 15
    # list_filter = ('collegeName', 'speicaltyName',)
    #禁用修改
    readonly_fields = [field.name for field in ArtsCollegeLine._meta.fields]
    list_filter = ['collegeName']
    def has_add_permission(self, request):
        # 禁用添加按钮
        return False
    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return False
admin.site.register(ArtsCollegeLine,ArtsCollegeLineAdmin)
#用于专业实力的导入导出
class MajorAbilityResource(resources.ModelResource):
    class Meta:
        model = MajorAbility
#专业实力
class MajorAbilityAdmin(ImportExportActionModelAdmin):
    list_display = ['collegeCode','collegeName','speicaltyName','specialtyPlace','specialtyComment','collegeCount','isKeyConstruction','specialtyLevelName']
    actions_on_top = True
    list_per_page = 15
    list_filter = ['speicaltyName']
    #禁用修改
    readonly_fields = [field.name for field in MajorAbility._meta.fields]
    def has_add_permission(self, request):
        # 禁用添加按钮
        return False
    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return False
admin.site.register(MajorAbility,MajorAbilityAdmin)
#用于学校信息的导入导出
class CollegeInfoResource(resources.ModelResource):
    class Meta:
        model = CollegeInfo
#学校信息
class CollegeInfoAdmin(ImportExportActionModelAdmin):
    list_display = ['collegeCode','collegeName','categoryName','propertyName','levelName','provinceName',
                    'cityName','address','url','phone','profile']
    actions_on_top = True
    list_per_page = 15
    list_filter = ['collegeName']
    #禁用修改
    readonly_fields = [field.name for field in CollegeInfo._meta.fields]
    def has_add_permission(self, request):
        # 禁用添加按钮
        return False
    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return False
admin.site.register(CollegeInfo,CollegeInfoAdmin)
#用于学校信息的导入导出
class SciEnrollResource(resources.ModelResource):
    class Meta:
        model = SciEnroll
#理科高校录取情况
class SciEnrollAdmin(ImportExportActionModelAdmin):
    list_display = ['collegeCode','collegeName','subject','sequence','historyProYear','realRecruitTotal',
                    'firstWishTotal','enrollProperty','firstWishSucTotal','secondWishSucTotal']
    actions_on_top = True
    list_per_page = 15
    list_filter = ['collegeName']
    #禁用修改
    readonly_fields = [field.name for field in SciEnroll._meta.fields]
    def has_add_permission(self, request):
        # 禁用添加按钮
        return False
    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return False
admin.site.register(SciEnroll,SciEnrollAdmin)
#用于学校信息的导入导出
class ArtsEnrollResource(resources.ModelResource):
    class Meta:
        model = ArtsEnroll
#文科高校录取情况
class ArtsEnrollAdmin(ImportExportActionModelAdmin):
    list_display = ['collegeCode','collegeName','subject','sequence','historyProYear','realRecruitTotal',
                    'firstWishTotal','enrollProperty','firstWishSucTotal','secondWishSucTotal']
    actions_on_top = True
    list_per_page = 15
    list_filter = ['collegeName']
    #禁用修改
    readonly_fields = [field.name for field in ArtsEnroll._meta.fields]
    def has_add_permission(self, request):
        # 禁用添加按钮
        return False
    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return False
admin.site.register(ArtsEnroll,ArtsEnrollAdmin)
#理科一分一段表
class SciYiFenYiDuanResource(resources.ModelResource):
    class Meta:
        model = SciYiFenYiDuan
class SciYiFenYiDuanAdmin(ImportExportActionModelAdmin):
    list_display = ['province','year','subject','score','num','rank']
    actions_on_top = True
    list_per_page = 15
    list_filter = ['year']
    #禁用修改
    readonly_fields = [field.name for field in SciYiFenYiDuan._meta.fields]
    def has_add_permission(self, request):
        # 禁用添加按钮
        return False
    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return False
admin.site.register(SciYiFenYiDuan,SciYiFenYiDuanAdmin)
#文科一分一段表
class ArtYiFenYiDuanResource(resources.ModelResource):
    class Meta:
        model = ArtYiFenYiDuan
class ArtYiFenYiDuanAdmin(ImportExportActionModelAdmin):
    list_display = ['province','year','subject','score','num','rank']
    actions_on_top = True
    list_per_page = 15
    list_filter = ['year']
    #禁用修改
    readonly_fields = [field.name for field in ArtYiFenYiDuan._meta.fields]
    def has_add_permission(self, request):
        # 禁用添加按钮
        return False
    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return False
admin.site.register(ArtYiFenYiDuan,ArtYiFenYiDuanAdmin)

#批次
class OrderResource(resources.ModelResource):
    class Meta:
        model = Order
class OrderAdmin(ImportExportActionModelAdmin):
    list_display = ['id','name','parentId']
    actions_on_top = True
    list_per_page = 15
    list_filter = ['name']
    #禁用修改
    readonly_fields = [field.name for field in Order._meta.fields]
    def has_add_permission(self, request):
        # 禁用添加按钮
        return False
    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return False
admin.site.register(Order,OrderAdmin)


# 省份
class ProvinceResource(resources.ModelResource):
    class Meta:
        model = Province
class ProvinceAdmin(ImportExportActionModelAdmin):
    list_display = ['id','provinceName']
    actions_on_top = True
    list_per_page = 15
    list_filter = ['provinceName']
    #禁用修改
    readonly_fields = [field.name for field in Province._meta.fields]
    def has_add_permission(self, request):
        # 禁用添加按钮
        return False
    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return False
admin.site.register(Province,ProvinceAdmin)


# 用户
class UserResource(resources.ModelResource):
    class Meta:
        model = User
class UserAdmin(ImportExportActionModelAdmin):
    list_display = ['userName','password']
    actions_on_top = True
    list_per_page = 15
    list_filter = ['userName']

admin.site.register(User,UserAdmin)

#理科录取计划
class SciPlanResource(resources.ModelResource):
    class Meta:
        model = SciPlan
class SciPlanAdmin(ImportExportActionModelAdmin):
    list_display = ['collegeName', 'province','code','subject','sequence','plan','isAdd','year']
    actions_on_top = True
    list_per_page = 15
    list_filter = ['collegeName','year']
    #禁用修改
    readonly_fields = [field.name for field in SciPlan._meta.fields]
    def has_add_permission(self, request):
        # 禁用添加按钮
        return False
    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return False
admin.site.register(SciPlan,SciPlanAdmin)

#文科录取计划
class ArtsPlanResource(resources.ModelResource):
    class Meta:
        model = ArtsPlan
class ArtsPlanAdmin(ImportExportActionModelAdmin):
    list_display = ['collegeName', 'province','code','subject','sequence','plan','isAdd','year']
    actions_on_top = True
    list_per_page = 15
    list_filter = ['collegeName','year']
    #禁用修改
    readonly_fields = [field.name for field in ArtsPlan._meta.fields]
    def has_add_permission(self, request):
        # 禁用添加按钮
        return False
    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return False
admin.site.register(ArtsPlan,ArtsPlanAdmin)

#招生简章
class EnrollmentGuldeResource(resources.ModelResource):
    class Meta:
        model = EnrollmentGulde
class EnrollmentGuldeAdmin(ImportExportActionModelAdmin):
    list_display = ['collegeCode', 'title','EnrollmentGulde']
    actions_on_top = True
    list_per_page = 15
    list_filter = ['title']
    #禁用修改
    readonly_fields = [field.name for field in EnrollmentGulde._meta.fields]
    def has_add_permission(self, request):
        # 禁用添加按钮
        return False
    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return False
admin.site.register(EnrollmentGulde,EnrollmentGuldeAdmin)

#专业库
class MajorInfoResource(resources.ModelResource):
    class Meta:
        model = MajorInfo
class MajorInfoAdmin(ImportExportActionModelAdmin):
    list_display = ['speicaltyName', 'categoryName','parentCategoryName','graduateScale','employInterval','specialtyLevelName']
    actions_on_top = True
    list_per_page = 15
    list_filter = ['speicaltyName','specialtyLevelName']
    #禁用修改
    readonly_fields = [field.name for field in MajorInfo._meta.fields]
    def has_add_permission(self, request):
        # 禁用添加按钮
        return False
    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return False
admin.site.register(MajorInfo,MajorInfoAdmin)