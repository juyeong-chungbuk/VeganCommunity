# Generated by Django 3.2 on 2021-06-28 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
