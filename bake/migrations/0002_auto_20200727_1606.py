# Generated by Django 2.2 on 2020-07-27 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bake', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='zipcode',
            field=models.IntegerField(),
        ),
    ]
