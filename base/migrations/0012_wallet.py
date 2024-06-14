# Generated by Django 5.0.6 on 2024-06-08 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_account_eroi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=10)),
                ('network', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
    ]