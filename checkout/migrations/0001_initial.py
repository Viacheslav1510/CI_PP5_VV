# Generated by Django 3.2 on 2023-04-25 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0004_alter_track_album'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(default='', editable=False, max_length=35)),
                ('full_name', models.CharField(default='', max_length=55)),
                ('email', models.EmailField(default='', max_length=254)),
                ('phone_number', models.CharField(default='', max_length=20)),
                ('address1', models.CharField(default='', max_length=85)),
                ('address2', models.CharField(blank=True, default='', max_length=85, null=True)),
                ('town_or_city', models.CharField(default='', max_length=45)),
                ('postcode', models.CharField(blank=True, default='', max_length=25, null=True)),
                ('county', models.CharField(blank=True, default='', max_length=85, null=True)),
                ('country', models.CharField(max_length=40)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('delivery_cost', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('order_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('grand_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('lineitem_total', models.DecimalField(decimal_places=2, editable=False, max_digits=6)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='checkout.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.album')),
            ],
        ),
    ]
