# Generated by Django 3.1.6 on 2021-02-03 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_campain_direction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campain',
            name='direction',
            field=models.CharField(choices=[('ltr', 'left to right'), ('rtl', 'right to left')], default='ltr', max_length=3),
        ),
    ]
