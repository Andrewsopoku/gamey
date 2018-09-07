# Generated by Django 2.0.7 on 2018-09-07 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0005_auto_20180907_1043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deposits',
            name='user',
        ),
        migrations.AddField(
            model_name='deposits',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]