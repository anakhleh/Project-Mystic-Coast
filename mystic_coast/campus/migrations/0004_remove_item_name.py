# Generated by Django 2.1.7 on 2019-04-02 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0003_auto_20190328_2139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='name',
        ),
    ]