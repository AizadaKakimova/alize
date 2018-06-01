# Generated by Django 2.0.4 on 2018-04-22 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alize', '0009_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=30, verbose_name='Имя пользователя')),
                ('body', models.TextField(verbose_name='Комментария')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
        ),
        migrations.RemoveField(
            model_name='comments',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
