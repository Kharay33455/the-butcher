# Generated by Django 5.0.6 on 2024-06-08 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_rename_acccount_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='multiplier',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=5),
        ),
    ]
