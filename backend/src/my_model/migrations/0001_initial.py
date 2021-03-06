# Generated by Django 4.0.3 on 2022-03-14 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('product_code', models.TextField()),
                ('visibility', models.BooleanField(blank=True)),
                ('currency_type', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('requester_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
