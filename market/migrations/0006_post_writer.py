# Generated by Django 3.2 on 2021-06-28 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_auto_20210627_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='writer',
            field=models.CharField(default='', max_length=100),
        ),
    ]
