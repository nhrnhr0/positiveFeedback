# Generated by Django 3.1.6 on 2021-02-03 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20210203_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campain',
            name='transitionIn',
            field=models.CharField(choices=[('0', 'slide in right'), ('1', 'slide in left')], default='0', max_length=1),
        ),
    ]
