from django.shortcuts import render

# Create your views here.
from rest_framework import views
from rest_framework import response
from web import models
from web.utils.serializers import *

##理科专业分数线view
class SciMajorLineView(views.APIView):
    def get(self,request):
        #查询所有
        SciMajorLine = models.SciMajorLine.objects.all()
        serializer = SciMajorLineSerializer(SciMajorLine,many=True)
        return response.Response({
            "code":0,
            "data":serializer.data
        })