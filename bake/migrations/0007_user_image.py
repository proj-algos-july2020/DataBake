# Generated by Django 2.2 on 2020-08-05 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bake', '0006_auto_20200802_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='https://i.ibb.co/FbSVkhk/Default.png', upload_to='profile_pics'),
        ),
    ]
