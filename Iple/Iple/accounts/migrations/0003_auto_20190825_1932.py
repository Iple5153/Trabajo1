# Generated by Django 2.2.4 on 2019-08-25 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190825_1509'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='Usuario',
            new_name='user',
        ),
    ]