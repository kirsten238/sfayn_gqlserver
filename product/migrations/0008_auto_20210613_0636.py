# Generated by Django 2.2.17 on 2021-06-13 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20210612_1408'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productvariant',
            old_name='primary',
            new_name='default',
        ),
    ]