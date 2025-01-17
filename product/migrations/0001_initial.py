# Generated by Django 2.2.17 on 2021-06-12 07:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.ProductCategory')),
            ],
        ),
        migrations.CreateModel(
            name='ProductParent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('parent_sn', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100, null=True)),
                ('goods_brand', models.CharField(max_length=30, null=True)),
                ('goods_desc', models.TextField(null=True)),
                ('status', models.IntegerField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cat2product', to='product.ProductCategory')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user2product', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductVideo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('video_url', models.CharField(max_length=100, null=True)),
                ('parent_sn', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent2video', to='product.ProductParent')),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariants',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sku', models.CharField(max_length=50)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('options', models.CharField(blank=True, max_length=50, null=True)),
                ('parent_sn', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product2variants', to='product.ProductParent')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('img_url', models.CharField(max_length=100, null=True)),
                ('cover_photo', models.IntegerField(default=False)),
                ('parent_sn', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent2image', to='product.ProductParent')),
            ],
        ),
    ]
