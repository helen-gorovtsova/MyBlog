# Generated by Django 3.2.7 on 2021-09-21 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210915_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_body',
            field=models.TextField(help_text='Введите текст поста сюда'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(help_text='Введите название поста', max_length=250),
        ),
    ]
