# Generated by Django 3.1.6 on 2021-02-02 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0007_auto_20210202_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campain',
            name='owner',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='proof',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='proofs'),
        ),
        migrations.AlterField(
            model_name='proof',
            name='owner',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
