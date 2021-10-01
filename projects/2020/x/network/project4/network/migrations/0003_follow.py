# Generated by Django 3.2.6 on 2021-10-01 23:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_alter_entry_poster'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('follow_id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('following', models.CharField(default=None, max_length=64)),
                ('followedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followerUsrName', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
