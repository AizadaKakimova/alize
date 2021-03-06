# Generated by Django 2.0.4 on 2018-04-22 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alize', '0012_auto_20180422_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='date',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='text',
        ),
        migrations.AddField(
            model_name='comment',
            name='body',
            field=models.TextField(default='Write your Comment', verbose_name='Комментарии'),
        ),
        migrations.AddField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.CharField(max_length=30, verbose_name='Имя пользователя'),
        ),
    ]
