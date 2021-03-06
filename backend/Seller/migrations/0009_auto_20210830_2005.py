# Generated by Django 3.2.6 on 2021-08-30 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0008_auto_20210830_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productorderdetails',
            name='CustomerId',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='CId', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='productorderdetails',
            name='ProductId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itemId', to='Seller.sellerproductdetails'),
        ),
    ]
