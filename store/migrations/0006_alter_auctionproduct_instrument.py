# Generated by Django 5.0.7 on 2024-09-11 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auctionproduct_instrument_alter_bid_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionproduct',
            name='instrument',
            field=models.CharField(default='', max_length=254),
        ),
    ]
