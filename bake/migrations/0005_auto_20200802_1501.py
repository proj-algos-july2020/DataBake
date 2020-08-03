# Generated by Django 2.2 on 2020-08-02 22:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bake', '0004_auto_20200801_2009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='categories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recipe_categories', to='bake.Recipe'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='cook_time',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='prep_time',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='ingredient_measurement',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='ingredient_quantity',
            field=models.FloatField(null=True),
        ),
    ]
