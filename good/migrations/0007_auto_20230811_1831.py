# Generated by Django 3.2.4 on 2023-08-11 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('good', '0006_auto_20230811_1722'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=4000, verbose_name='url name')),
                ('simple_price', models.CharField(max_length=40, verbose_name='oddiy tarif')),
                ('premium', models.CharField(max_length=40, verbose_name='premium tarif')),
                ('platinum', models.CharField(max_length=40, verbose_name='yuqori  tarif')),
            ],
            options={
                'verbose_name': 'Url va Narxlar online_dars',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ChangePrices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=4000, verbose_name='url name')),
                ('simple_price', models.CharField(max_length=40, verbose_name='oddiy tarif')),
                ('premium', models.CharField(max_length=40, verbose_name='premium tarif')),
                ('platinum', models.CharField(max_length=40, verbose_name='yuqori  tarif')),
            ],
            options={
                'verbose_name': 'Narxlar savdo-robot',
                'ordering': ['id'],
            },
        ),
        migrations.AlterModelOptions(
            name='change',
            options={'ordering': ['id'], 'verbose_name': 'Url va Narxlar discord'},
        ),
    ]