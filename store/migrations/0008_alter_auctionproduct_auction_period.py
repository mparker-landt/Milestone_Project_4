# Generated by Django 5.0.7 on 2024-09-11 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_auctionproduct_bidders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionproduct',
            name='auction_period',
            field=models.DateField(),
        ),
    ]
