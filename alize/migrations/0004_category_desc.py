# Generated by Django 2.0.4 on 2018-04-17 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alize', '0003_category_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='desc',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
    ]
