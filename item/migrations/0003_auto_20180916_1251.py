# Generated by Django 2.0 on 2018-09-16 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_item_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='number',
            field=models.CharField(max_length=20, verbose_name='番号'),
        ),
    ]
