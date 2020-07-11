# Generated by Django 3.0.3 on 2020-06-23 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20200623_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='majorability',
            name='collegeCode',
            field=models.IntegerField(blank=True, max_length=8, null=True, verbose_name='学校编码'),
        ),
        migrations.AlterField(
            model_name='majorability',
            name='collegeCount',
            field=models.IntegerField(blank=True, max_length=6, null=True, verbose_name='开设院校数'),
        ),
        migrations.AlterField(
            model_name='majorability',
            name='specialtyCode',
            field=models.IntegerField(blank=True, max_length=10, null=True, verbose_name='专业编码'),
        ),
        migrations.AlterField(
            model_name='majorability',
            name='specialtyComment',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='专业级别'),
        ),
        migrations.AlterField(
            model_name='majorability',
            name='specialtyPlace',
            field=models.IntegerField(blank=True, max_length=5, null=True, verbose_name='专业名次'),
        ),
        migrations.AlterField(
            model_name='majorability',
            name='speicaltyName',
            field=models.CharField(blank=True, max_length=130, null=True, verbose_name='专业名称'),
        ),
    ]
