# Generated by Django 3.2.5 on 2022-01-23 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_auto_20220118_0920'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='remark',
            field=models.CharField(default='', max_length=100, verbose_name='Remark'),
        ),
    ]
