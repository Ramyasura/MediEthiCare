# Generated by Django 5.0.1 on 2024-02-08 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0015_alter_medicine_medicine_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='admin_status',
            field=models.CharField(default='pending', max_length=15),
        ),
    ]
