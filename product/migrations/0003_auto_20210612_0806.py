# Generated by Django 2.2.17 on 2021-06-12 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20210612_0746'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductVariants',
            new_name='ProductVariant',
        ),
    ]
