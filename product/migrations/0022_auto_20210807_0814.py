# Generated by Django 3.2.4 on 2021-08-07 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_auto_20210804_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productparent',
            name='img_upload',
        ),
        migrations.RemoveField(
            model_name='productparent',
            name='img_url',
        ),
        migrations.RemoveField(
            model_name='productparent',
            name='max_price',
        ),
        migrations.RemoveField(
            model_name='productparent',
            name='min_price',
        ),
        migrations.RemoveField(
            model_name='productparent',
            name='totalQty',
        ),
    ]