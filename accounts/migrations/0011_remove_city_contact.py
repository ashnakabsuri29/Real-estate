# Generated by Django 3.2 on 2021-05-24 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_flats_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='contact',
        ),
    ]