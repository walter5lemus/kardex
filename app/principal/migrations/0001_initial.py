# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-11 02:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('concepto', models.CharField(max_length=200)),
                ('entrada', models.IntegerField(blank=True, null=True)),
                ('salida', models.IntegerField(blank=True, null=True)),
                ('saldo', models.IntegerField()),
                ('codigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Producto')),
            ],
        ),
    ]
