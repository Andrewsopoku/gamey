# Generated by Django 2.0.7 on 2018-08-29 15:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_auto_20180829_1455'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gains',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=4, max_digits=8)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='monthlyinterest',
            name='deposit',
        ),
        migrations.DeleteModel(
            name='MonthlyInterest',
        ),
    ]
