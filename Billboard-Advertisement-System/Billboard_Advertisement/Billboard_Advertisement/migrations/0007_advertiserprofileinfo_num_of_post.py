# Generated by Django 2.2.17 on 2021-09-11 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Billboard_Advertisement', '0006_auto_20210911_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertiserprofileinfo',
            name='num_of_post',
            field=models.IntegerField(default=0),
        ),
    ]
