# Generated by Django 4.0 on 2021-12-24 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_elements_discovery_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elements',
            name='boiling_point',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='elements',
            name='melting_point',
            field=models.CharField(max_length=15),
        ),
    ]
