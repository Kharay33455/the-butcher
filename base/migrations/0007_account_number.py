# Generated by Django 5.0.6 on 2024-06-08 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_level_multiplier'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='number',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
