# Generated by Django 3.2.6 on 2021-08-15 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_alter_listing_creator'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('ammount', models.FloatField(help_text='Enter ammount to bid')),
                ('bidder', models.CharField(default='None', help_text='Enter username of bidder', max_length=64)),
                ('location', models.CharField(default='None', help_text='Enter the name of listing to bid on', max_length=64)),
            ],
        ),
    ]
