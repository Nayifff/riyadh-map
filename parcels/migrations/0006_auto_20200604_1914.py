# Generated by Django 3.0.6 on 2020-06-04 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcels', '0005_auto_20200604_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='date',
            field=models.CharField(max_length=256),
        ),
    ]