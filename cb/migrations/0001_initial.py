# Generated by Django 2.2 on 2019-04-21 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('sku', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('status', models.IntegerField(null=True)),
                ('title', models.CharField(max_length=100, null=True)),
                ('encrypted_sku', models.CharField(max_length=50, null=True)),
                ('color', models.CharField(max_length=10, null=True)),
                ('size', models.CharField(max_length=5, null=True)),
                ('ship_weight', models.FloatField(null=True)),
                ('volume_weight', models.FloatField(null=True)),
                ('cat_id', models.IntegerField(null=True)),
                ('parent_id', models.IntegerField(null=True)),
                ('goods_brand', models.CharField(max_length=30, null=True)),
                ('purchase_title', models.CharField(max_length=100, null=True)),
                ('package_length', models.FloatField(null=True)),
                ('package_width', models.FloatField(null=True)),
                ('package_height', models.FloatField(null=True)),
                ('size_chart', models.CharField(max_length=100, null=True)),
                ('convert_size_chart', models.CharField(max_length=100, null=True)),
                ('packing_expense', models.FloatField(null=True)),
                ('forbid_platform', models.CharField(max_length=25, null=True)),
                ('permit_platform', models.CharField(max_length=25, null=True)),
                ('forbid_region', models.CharField(max_length=25, null=True)),
                ('permit_region', models.CharField(max_length=25, null=True)),
                ('goods_nature', models.CharField(max_length=5, null=True)),
                ('shipping_attributes', models.CharField(max_length=25, null=True)),
                ('goods_desc', models.TextField(null=True)),
                ('last_update', models.DateField(null=True)),
                ('is_amazon_select', models.IntegerField(null=True)),
                ('video_url', models.CharField(max_length=50, null=True)),
                ('hs_code', models.CharField(max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductWarehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=250, null=True)),
                ('warehouse', models.CharField(max_length=15, null=True)),
                ('price', models.FloatField(null=True)),
                ('is_clearance', models.IntegerField(null=True)),
                ('clearance_price', models.FloatField(null=True)),
                ('is_promote', models.IntegerField(null=True)),
                ('promote_price', models.FloatField(null=True)),
                ('promote_cancel_time', models.CharField(max_length=100, null=True)),
                ('is_new', models.IntegerField(null=True)),
                ('new_price', models.FloatField(null=True)),
                ('new_stock', models.IntegerField(null=True)),
                ('new_stock_total', models.IntegerField(null=True)),
                ('handling_fee', models.FloatField(null=True)),
                ('sale_time', models.DateField(null=True)),
                ('goods_state', models.CharField(max_length=50, null=True)),
                ('purchase_info', models.CharField(max_length=400, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='warehouse', to='cb.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductOriginalImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_img', models.CharField(max_length=250, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='original_img', to='cb.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('map', models.CharField(max_length=50, null=True)),
                ('currency', models.CharField(max_length=25, null=True)),
                ('limit_price', models.FloatField(null=True)),
                ('platform', models.CharField(max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='map', to='cb.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductDescImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_img', models.CharField(max_length=250, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='desc_img', to='cb.Product')),
            ],
        ),
    ]
