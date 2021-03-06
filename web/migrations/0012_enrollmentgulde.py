# Generated by Django 3.0.3 on 2020-07-08 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_artsplan'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnrollmentGulde',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collegeCode', models.IntegerField(verbose_name='学校编码')),
                ('title', models.CharField(blank=True, max_length=64, null=True, verbose_name='标题')),
                ('content', models.TextField(blank=True, null=True, verbose_name='内容')),
            ],
            options={
                'verbose_name': '招生简章',
                'verbose_name_plural': '招生简章',
                'ordering': ('collegeCode',),
            },
        ),
    ]
