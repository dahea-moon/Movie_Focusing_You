# Generated by Django 2.2.7 on 2019-11-27 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20191126_1917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_keyword',
            name='keyword',
        ),
        migrations.RemoveField(
            model_name='user_keyword',
            name='user',
        ),
        migrations.DeleteModel(
            name='Movie_Keyword',
        ),
        migrations.DeleteModel(
            name='User_Keyword',
        ),
    ]