# Generated by Django 2.2.17 on 2021-09-11 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Billboard_Advertisement', '0007_advertiserprofileinfo_num_of_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertiserprofileinfo',
            name='num_of_post',
        ),
    ]
