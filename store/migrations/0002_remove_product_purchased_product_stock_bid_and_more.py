# Generated by Django 5.0.7 on 2024-09-12 13:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_rename_default_county_userprofile_billing_county_and_more'),
        ('store', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='purchased',
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=6),
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('buyer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='auction_buyer', to='profiles.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='AuctionProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('description', models.TextField()),
                ('instrument', models.CharField(default='', max_length=254)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('condition', models.CharField(choices=[('new', 'New / Never Opened'), ('refurbished', 'Refurbished'), ('mint_condition', 'Mint Condition'), ('good_condition', 'Good Condition'), ('poor_condition', 'Poor Condition')], max_length=20)),
                ('base_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('auction_period', models.DateField()),
                ('purchased', models.BooleanField(blank=True, default=False, null=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('seller', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='auction_seller', to='profiles.userprofile')),
                ('bidders', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bid', to='store.bid')),
            ],
            options={
                'verbose_name_plural': 'Auctions',
            },
        ),
        migrations.CreateModel(
            name='RentalProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_sku', models.CharField(blank=True, max_length=254, null=True)),
                ('rental_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('rental_period', models.DateField()),
                ('rental_stock', models.DecimalField(decimal_places=0, default=0, max_digits=6)),
                ('has_premium', models.BooleanField(blank=True, default=False, null=True)),
                ('premium', models.BooleanField(blank=True, default=False, null=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.product')),
            ],
            options={
                'verbose_name_plural': 'Rentals',
            },
        ),
    ]
