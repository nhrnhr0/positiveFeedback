# Generated by Django 3.1.6 on 2021-02-04 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_proof_starts'),
    ]

    operations = [
        migrations.AddField(
            model_name='proof',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='link'),
        ),
    ]
