# Generated by Django 2.2.7 on 2020-05-08 05:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0008_einfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]