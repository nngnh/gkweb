# Generated by Django 3.0.3 on 2020-07-07 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_usertoken'),
    ]

    operations = [
        migrations.CreateModel(
            name='SciPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collegeName', models.CharField(blank=True, max_length=32, null=True, verbose_name='学校名称')),
                ('province', models.CharField(blank=True, max_length=8, null=True, verbose_name='省份')),
                ('code', models.IntegerField(blank=True, null=True, verbose_name='招生代码')),
                ('subject', models.CharField(blank=True, max_length=8, null=True, verbose_name='科类')),
                ('sequence', models.CharField(blank=True, max_length=32, null=True, verbose_name='批次')),
                ('plan', models.IntegerField(blank=True, null=True, verbose_name='计划数')),
                ('isAdd', models.BooleanField(blank=True, null=True, verbose_name='是否新增')),
                ('year', models.IntegerField(blank=True, null=True, verbose_name='年')),
            ],
            options={
                'verbose_name': '招生计划',
                'verbose_name_plural': '招生计划',
            },
        ),
    ]
