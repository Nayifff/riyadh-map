# Generated by Django 3.0.6 on 2020-05-29 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcels', '0003_auto_20200529_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planid', models.CharField(max_length=256)),
                ('description', models.CharField(default='residential', max_length=256)),
                ('price', models.CharField(max_length=256)),
                ('date', models.CharField(max_length=256)),
            ],
        ),
    ]