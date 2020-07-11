# Generated by Django 3.0.3 on 2020-07-02 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_province'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=64)),
                ('userName', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='web.User')),
            ],
        ),
    ]
