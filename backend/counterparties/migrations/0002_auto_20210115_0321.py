# Generated by Django 3.1.5 on 2021-01-15 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('counterparties', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='counterparties',
            name='manager',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='counterparties.manager'),
        ),
        migrations.AlterField(
            model_name='counterparties',
            name='address_from',
            field=models.CharField(max_length=1024, verbose_name='Адрес VLAN От'),
        ),
        migrations.AlterField(
            model_name='counterparties',
            name='address_to',
            field=models.CharField(max_length=1024, verbose_name='До'),
        ),
        migrations.AlterField(
            model_name='counterparties',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Наименование контрагента'),
        ),
        migrations.AlterField(
            model_name='counterparties',
            name='vip',
            field=models.BooleanField(default=False, verbose_name='ВИП Клиент'),
        ),
    ]