# Generated by Django 3.1.6 on 2021-02-04 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20210204_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='proof',
            name='starts',
            field=models.FloatField(default=4.5, verbose_name='starts (-1 to deactivate)'),
        ),
    ]
