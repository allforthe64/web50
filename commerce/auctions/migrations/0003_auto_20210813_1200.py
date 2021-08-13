# Generated by Django 3.2.6 on 2021-08-13 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_listing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='descrpt',
            new_name='description',
        ),
        migrations.AddField(
            model_name='listing',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='beginningBid',
            field=models.FloatField(help_text='Enter minimum price of item'),
        ),
    ]
