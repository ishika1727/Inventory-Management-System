# Generated by Django 2.2.6 on 2019-11-05 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20191105_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='bill_id',
            field=models.CharField(default='tkhzfinuga', max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_id',
            field=models.CharField(default='kafqtkmprh', max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='item_id',
            field=models.CharField(default='fiwdnamggz', max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='login',
            name='login_id',
            field=models.OneToOneField(default='hkzutersyr', on_delete=django.db.models.deletion.CASCADE, to='main.CustomUser'),
        ),
        migrations.AlterField(
            model_name='role',
            name='role_id',
            field=models.CharField(default='pcofipdcfj', max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='salesandpurchases',
            name='transaction_id',
            field=models.CharField(default='opoyeumigf', max_length=10, primary_key=True, serialize=False),
        ),
    ]
