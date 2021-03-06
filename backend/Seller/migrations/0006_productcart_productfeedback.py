# Generated by Django 3.2.6 on 2021-08-29 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0005_alter_sellerproductdetails_pphoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductFeedback',
            fields=[
                ('FeedbackId', models.AutoField(primary_key=True, serialize=False)),
                ('AddFeedback', models.TextField(max_length=1000)),
                ('Rating', models.BigIntegerField()),
                ('CustomerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ProductId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Seller.sellerproductdetails')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCart',
            fields=[
                ('CartId', models.AutoField(primary_key=True, serialize=False)),
                ('Quantity', models.BigIntegerField()),
                ('CDate', models.DateTimeField(auto_now_add=True)),
                ('ProductId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Seller.sellerproductdetails')),
                ('id', models.ForeignKey(default='0000', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
