# Generated by Django 2.2.7 on 2019-11-26 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20191126_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rates',
            field=models.ManyToManyField(related_name='rated_user', through='movies.Rating', to='movies.Movie'),
        ),
        migrations.AlterField(
            model_name='user',
            name='watchedlist',
            field=models.ManyToManyField(related_name='watched_users', to='movies.Movie'),
        ),
        migrations.AlterField(
            model_name='user',
            name='wishlist',
            field=models.ManyToManyField(related_name='wished_users', to='movies.Movie'),
        ),
    ]
