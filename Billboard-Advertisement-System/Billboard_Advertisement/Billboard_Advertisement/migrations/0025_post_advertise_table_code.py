# Generated by Django 3.2 on 2021-07-30 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Billboard_Advertisement', '0024_rename_totalamount_confirm_post_adcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_advertise_table',
            name='code',
            field=models.CharField(default='1', max_length=100),
            preserve_default=False,
        ),
    ]