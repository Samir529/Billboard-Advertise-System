# Generated by Django 3.2 on 2021-07-30 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Billboard_Advertisement', '0023_confirm_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='confirm_post',
            old_name='totalAmount',
            new_name='adCode',
        ),
    ]