# Generated by Django 4.2.4 on 2023-09-05 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='country',
        ),
        migrations.RemoveField(
            model_name='user',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='f_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='industry',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='user',
            name='kyc_approved',
        ),
        migrations.RemoveField(
            model_name='user',
            name='l_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='pin_code',
        ),
        migrations.RemoveField(
            model_name='user',
            name='verified_user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='wallet_balance',
        ),
        migrations.RemoveField(
            model_name='user',
            name='wiremi_id',
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('IS_SUPERUSER', 'IS_SUPERUSER'), ('IS_STAFF', 'IS_STAFF'), ('IS_CUSTOMER', 'IS_CUSTOMER')], max_length=64),
        ),
    ]
