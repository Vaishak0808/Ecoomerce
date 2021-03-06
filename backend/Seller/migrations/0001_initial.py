# Generated by Django 3.2.6 on 2021-08-18 13:54

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationDataTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('Address', models.CharField(max_length=500)),
                ('PhoneNumber', models.BigIntegerField()),
                ('Pincode', models.BigIntegerField()),
                ('Updated_on', models.DateTimeField(auto_now=True)),
                ('UserType', models.CharField(default='Customer', max_length=200)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='SellerRegistration',
            fields=[
                ('CompanyId', models.AutoField(primary_key=True, serialize=False)),
                ('CompanyName', models.CharField(max_length=200)),
                ('CompanyAddress', models.TextField(max_length=200)),
                ('CompanyPhonenumber', models.BigIntegerField()),
                ('CompanyPin', models.BigIntegerField()),
                ('Proof', models.FileField(default=True, null=True, upload_to='SellerProofs/')),
                ('CompanyWebsite', models.CharField(max_length=200, null=True)),
                ('CompanyEmail', models.CharField(max_length=200, null=True)),
                ('Status', models.BooleanField(default=False)),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userid', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SellerProductDetails',
            fields=[
                ('ProductId', models.AutoField(primary_key=True, serialize=False)),
                ('PCategory', models.CharField(max_length=200)),
                ('PName', models.CharField(max_length=200)),
                ('PDescription', models.TextField(max_length=2000)),
                ('PPrice', models.CharField(max_length=100)),
                ('PPhoto', models.ImageField(upload_to='ProductImages/')),
                ('sellername', models.CharField(default=False, max_length=200)),
                ('Seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Seller.sellerregistration')),
            ],
        ),
        migrations.CreateModel(
            name='ProductOrderDetails',
            fields=[
                ('OrderId', models.AutoField(primary_key=True, serialize=False)),
                ('Quantity', models.CharField(max_length=200)),
                ('OrderDate', models.DateField(auto_now_add=True)),
                ('OrderStatus', models.CharField(default='Ordered', max_length=200)),
                ('CustomerId', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ProductId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Seller.sellerproductdetails')),
            ],
        ),
    ]
