# Generated by Django 3.2.6 on 2021-08-29 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0006_productcart_productfeedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcart',
            name='ProductId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PId', to='Seller.sellerproductdetails'),
        ),
        migrations.AlterField(
            model_name='productcart',
            name='id',
            field=models.ForeignKey(default='0000', on_delete=django.db.models.deletion.CASCADE, related_name='CustomerId', to=settings.AUTH_USER_MODEL),
        ),
    ]