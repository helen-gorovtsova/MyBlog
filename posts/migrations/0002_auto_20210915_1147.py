# Generated by Django 3.2.7 on 2021-09-15 11:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='posts.post'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_data',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]