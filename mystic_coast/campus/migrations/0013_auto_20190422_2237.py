# Generated by Django 2.1.7 on 2019-04-23 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0012_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='favorite_restaurant_list',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
