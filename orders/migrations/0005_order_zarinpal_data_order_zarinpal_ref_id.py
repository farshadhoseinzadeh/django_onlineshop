# Generated by Django 4.2.16 on 2024-11-21 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_zarinpal_authority'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='zarinpal_data',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='zarinpal_ref_id',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]