# Generated by Django 5.0.7 on 2024-09-12 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_enquiry_enquiry_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='enquiry_number',
            field=models.CharField(editable=False, max_length=32),
        ),
    ]
