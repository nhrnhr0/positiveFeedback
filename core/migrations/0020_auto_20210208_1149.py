# Generated by Django 3.1.6 on 2021-02-08 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20210208_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campain',
            name='backgroundColor',
            field=models.TextField(default='#ffffff'),
        ),
        migrations.AlterField(
            model_name='campain',
            name='headingColor',
            field=models.TextField(default='#000000'),
        ),
        migrations.AlterField(
            model_name='campain',
            name='textColor',
            field=models.TextField(default='#333333'),
        ),
    ]