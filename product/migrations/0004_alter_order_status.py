# Generated by Django 3.2.13 on 2022-06-13 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'PENDING'), ('Out for delivery', 'OUT FOR DELIVERY'), ('Delivery', 'DELIVERY')], max_length=50, null=True),
        ),
    ]
