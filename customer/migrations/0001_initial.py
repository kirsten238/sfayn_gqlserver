# Generated by Django 2.2.17 on 2021-06-16 12:37

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
            name='CustomerAddress',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50, null=True)),
                ('address', models.TextField()),
                ('postal', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('default', models.IntegerField(blank=True, default=False, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user2addr', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]