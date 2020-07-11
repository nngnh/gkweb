from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from web import views

drf_urlpatterns = [
    #学校信息
    url(r'^collegeinfo/$',view=views.CollegeInfoListView.as_view()),
    url(r'^collegeinfo/(?P<pk>\d+)$',view=views.CollegeInfoView.as_view()),
    #理科调档线信息
    url(r'^scicollegeline/$', view=views.SciCollegeLineListView.as_view()),
    url(r'^scicollegeline/(?P<pk>\d+)$', view=views.SciCollegeLineView.as_view()),
    #理科专业录取信息
    url(r'^scimajorline/(?P<pk>\d+)$',view=views.SciMajorLineView.as_view()),
    #文科调档线信息
    url(r'^artscollegeline/$',view=views.ArtsCollegeLineListView.as_view()),
    url(r'^artscollegeline/(?P<pk>\d+)$', view=views.ArtsCollegeLineView.as_view()),
    # 文科专业录取信息
    url(r'^artsmajorline/(?P<pk>\d+)$', view=views.ArtsMajorLineView.as_view()),
    #批次信息
    url(r'^order/$',view=views.OrderListView.as_view()),
    #省份
    url(r'^province/$',view=views.ProvinceView.as_view()),
    #登录认证
    url(r'^login/$',view=views.Login.as_view()),
    #预测学校
    url(r'^forecastcollege/$',view=views.ForecastCollegeView.as_view()),
    #预测专业
    url(r'^forecastmajor/$',view=views.ForecastMajorView.as_view()),
    #查询专业实力
    url(r'^majorability/(?P<pk>\d+)$',view=views.MajorAbilityView.as_view()),
    #理科高校录取情况
    url(r'^scienroll/(?P<pk>\d+)$',view=views.SciEnrollView.as_view()),
    #文科高校录取情况
    url(r'^artsenroll/(?P<pk>\d+)$',view=views.ArtsEnrollView.as_view()),
    #招生简章
    url(r'^enrollmentgulde/(?P<pk>\d+)$',view=views.EnrollmentGuldeView.as_view()),
    #专业库一级菜单
    url(r'^onemajorinfo/$',view=views.OneMajorInfoView.as_view()),
    #专业库二级菜单
    url(r'^twomajorinfo/$',view=views.TwoMajorInfoView.as_view()),
    #专业库三级菜单
    url(r'^threemajorinfo/$',view=views.ThreeMajorInfoView.as_view()),
    # 根据专业查询开设学校的信息
    url(r'^majortocollege/$', view=views.Major2CollegeView.as_view()),
    # 根据专业查询开设学校的信息
    url(r'^majorinfo/$', view=views.MajorView.as_view()),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'api/v1/',include(drf_urlpatterns)),
]

