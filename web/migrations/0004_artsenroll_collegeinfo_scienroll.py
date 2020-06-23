# Generated by Django 3.0.3 on 2020-06-22 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_artscollegeline_majorability_scicollegeline'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtsEnroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collegeCode', models.IntegerField(max_length=6, verbose_name='学校编码')),
                ('collegeHistoryId', models.IntegerField(max_length=6)),
                ('province', models.CharField(max_length=16, verbose_name='省份')),
                ('collegeName', models.CharField(max_length=100, verbose_name='学校名称')),
                ('subject', models.CharField(max_length=8, verbose_name='类别')),
                ('sequence', models.CharField(max_length=100, verbose_name='批次')),
                ('historyProYear', models.IntegerField(max_length=5, verbose_name='年')),
                ('realRecruitTotal', models.IntegerField(max_length=7, verbose_name='实际招生人数')),
                ('firstWishTotal', models.IntegerField(max_length=8, verbose_name='批线上第一 志愿报考数')),
                ('enrollProperty', models.CharField(max_length=7, verbose_name='录取性质')),
                ('firstWishSucTotal', models.IntegerField(max_length=7, verbose_name='第一志愿录取数')),
                ('secondWishSucTotal', models.IntegerField(max_length=7, verbose_name='其他志愿录取数')),
            ],
        ),
        migrations.CreateModel(
            name='CollegeInfo',
            fields=[
                ('collegeCode', models.AutoField(primary_key=True, serialize=False, verbose_name='学校编码')),
                ('collegeName', models.CharField(max_length=100, verbose_name='学校名称')),
                ('categoryName', models.CharField(max_length=5, verbose_name='类型')),
                ('propertyName', models.CharField(max_length=8, verbose_name='性质')),
                ('levelName', models.CharField(max_length=100, verbose_name='级别')),
                ('provinceName', models.CharField(max_length=16, verbose_name='省份')),
                ('cityName', models.CharField(max_length=16, verbose_name='城市')),
                ('address', models.CharField(max_length=150, verbose_name='地址')),
                ('url', models.CharField(max_length=100, verbose_name='学校官网')),
                ('phone', models.CharField(max_length=100, verbose_name='招生电话')),
                ('introduce', models.TextField(verbose_name='学校简介')),
            ],
        ),
        migrations.CreateModel(
            name='SciEnroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collegeCode', models.IntegerField(max_length=6, verbose_name='学校编码')),
                ('collegeHistoryId', models.IntegerField(max_length=6)),
                ('province', models.CharField(max_length=16, verbose_name='省份')),
                ('collegeName', models.CharField(max_length=100, verbose_name='学校名称')),
                ('subject', models.CharField(max_length=8, verbose_name='类别')),
                ('sequence', models.CharField(max_length=100, verbose_name='批次')),
                ('historyProYear', models.IntegerField(max_length=5, verbose_name='年')),
                ('realRecruitTotal', models.IntegerField(max_length=7, verbose_name='实际招生人数')),
                ('firstWishTotal', models.IntegerField(max_length=8, verbose_name='批线上第一 志愿报考数')),
                ('enrollProperty', models.CharField(max_length=7, verbose_name='录取性质')),
                ('firstWishSucTotal', models.IntegerField(max_length=7, verbose_name='第一志愿录取数')),
                ('secondWishSucTotal', models.IntegerField(max_length=7, verbose_name='其他志愿录取数')),
            ],
        ),
    ]