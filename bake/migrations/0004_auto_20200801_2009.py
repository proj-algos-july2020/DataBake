# Generated by Django 2.2 on 2020-08-02 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bake', '0003_auto_20200801_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='ingredient_measurement',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='ingredient_quantity',
            field=models.CharField(max_length=5),
        ),
    ]
