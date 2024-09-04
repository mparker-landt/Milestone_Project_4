# Generated by Django 5.0.7 on 2024-09-03 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
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
    ]
