from django.contrib import admin
from web.models import  *

admin.site.site_header = '高考数据管理系统'
admin.site.site_title = '高考数据管理系统'
admin.site.index_title = u'高考数据管理系统'


#理科专业分数线
class SciMajorLineAdmin(admin.ModelAdmin):
    #显示需要显示的字段
    list_display = ['collegeCode','province','collegeName','subject','sequence','year','speicaltyName',
                    'matricGrade','specialtyGradeDiff','matricGradePosition','positionMatricGrade',
                    'averageGrade','averageGradeDiff','averageGradePosition','positionAverageGrade']
    actions_on_top = True
    list_per_page = 15
    list_filter = ('collegeName', 'speicaltyName',)
    # search_fields = ['collegeName','speicaltyName']
    def has_add_permission(self, request):
        # 禁用添加按钮
        return False
    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return False
admin.site.register(SciMajorLine,SciMajorLineAdmin)

#文科专业分数线
class ArtsMajorLineAdmin(admin.ModelAdmin):
    #显示需要显示的字段
    list_display = ['collegeCode','province','collegeName','subject','sequence','year','speicaltyName',
                    'matricGrade','specialtyGradeDiff','matricGradePosition','positionMatricGrade',
                    'averageGrade','averageGradeDiff','averageGradePosition','positionAverageGrade']
    actions_on_top = True
    list_per_page = 15
    list_filter = ('collegeName', 'speicaltyName',)
    # search_fields = ['collegeName','speicaltyName']
    def has_add_permission(self, request):
        # 禁用添加按钮
        return False
    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return False
admin.site.register(ArtsMajorLine,ArtsMajorLineAdmin)


#理科调档线
class SciCollegeLineAdmin(admin.ModelAdmin):
    #显示需要显示的字段
    list_display = ['collegeCode','province','collegeName','subject','sequence','year','moveDocGrade',
                    'averageGrade','moveDocGradeDiff','averageGradeDiff','moveDocLocation',
                    'positionMoveDocGrade','averageLocation','positionAverageGrade']
    actions_on_top = True
    list_per_page = 15
    # list_filter = ('collegeName', 'speicaltyName',)
    search_fields = ['collegeName']
    def has_add_permission(self, request):
        # 禁用添加按钮
        return False
    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return False
admin.site.register(SciCollegeLine,SciCollegeLineAdmin)\

#文科调档线
class ArtsCollegeLineAdmin(admin.ModelAdmin):
    #显示需要显示的字段
    list_display = ['collegeCode','province','collegeName','subject','sequence','year','moveDocGrade',
                    'averageGrade','moveDocGradeDiff','averageGradeDiff','moveDocLocation',
                    'positionMoveDocGrade','averageLocation','positionAverageGrade']
    actions_on_top = True
    list_per_page = 15
    # list_filter = ('collegeName', 'speicaltyName',)
    search_fields = ['collegeName']
    def has_add_permission(self, request):
        # 禁用添加按钮
        return False
    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return False
admin.site.register(ArtsCollegeLine,ArtsCollegeLineAdmin)

#专业实力
class MajorAbilityAdmin(admin.ModelAdmin):
    list_display = ['collegeCode','collegeName','speicaltyName','specialtyPlace','specialtyComment','collegeCount','isKeyConstruction']
    actions_on_top = True
    list_per_page = 15

    def has_add_permission(self, request):
        # 禁用添加按钮
        return False
    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return False
admin.site.register(MajorAbility,MajorAbilityAdmin)

#学校信息
class CollegeInfoAdmin(admin.ModelAdmin):
    list_display = ['collegeCode','collegeName','categoryName','propertyName','levelName','provinceName',
                    'cityName','address','url','phone','introduce']
    actions_on_top = True
    list_per_page = 15

    def has_add_permission(self, request):
        # 禁用添加按钮
        return False
    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return False
admin.site.register(CollegeInfo,CollegeInfoAdmin)

#理科高校录取情况
class SciEnrollAdmin(admin.ModelAdmin):
    list_display = ['collegeCode','collegeName','subject','sequence','historyProYear','realRecruitTotal',
                    'firstWishTotal','enrollProperty','firstWishSucTotal','secondWishSucTotal']
    actions_on_top = True
    list_per_page = 15

    def has_add_permission(self, request):
        # 禁用添加按钮
        return False
    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return False
admin.site.register(SciEnroll,SciEnrollAdmin)

#文科高校录取情况
class ArtsEnrollAdmin(admin.ModelAdmin):
    list_display = ['collegeCode','collegeName','subject','sequence','historyProYear','realRecruitTotal',
                    'firstWishTotal','enrollProperty','firstWishSucTotal','secondWishSucTotal']
    actions_on_top = True
    list_per_page = 15
    def has_add_permission(self, request):
        # 禁用添加按钮
        return False
    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return False
admin.site.register(ArtsEnroll,ArtsEnrollAdmin)