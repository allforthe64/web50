# Generated by Django 3.2.6 on 2021-10-02 00:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_follow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='followedBy',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='followerUsrName', to=settings.AUTH_USER_MODEL),
        ),
    ]
