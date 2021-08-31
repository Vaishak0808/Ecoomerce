# Generated by Django 3.2.6 on 2021-08-30 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0007_auto_20210829_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='productorderdetails',
            name='Address',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='productorderdetails',
            name='TotalPrice',
            field=models.CharField(default=False, max_length=100),
        ),
    ]