# Generated by Django 3.0.6 on 2020-05-29 16:54

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parcels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcelinfo',
            name='coords',
            field=django.contrib.gis.db.models.fields.PolygonField(srid=4326),
        ),
    ]
