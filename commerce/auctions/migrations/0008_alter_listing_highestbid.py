# Generated by Django 3.2.6 on 2021-08-19 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_alter_listing_highestbid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='highestBid',
            field=models.FloatField(default=0),
        ),
    ]
