# Generated by Django 2.2 on 2020-07-26 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_title', models.CharField(max_length=255)),
                ('recipe_directions', models.TextField()),
                ('prep_time', models.CharField(max_length=20)),
                ('cook_time', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('zipcode', models.IntegerField(max_length=5)),
                ('state', models.CharField(max_length=2)),
                ('city', models.CharField(max_length=75)),
                ('email', models.CharField(max_length=255)),
                ('user_name', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('bio', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overall', models.IntegerField()),
                ('flavor', models.IntegerField()),
                ('difficulty', models.IntegerField()),
                ('accessibility', models.IntegerField()),
                ('survey_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('surveys', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_surveys', to='bake.Recipe')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='added_by',
            field=models.ManyToManyField(related_name='added_recipes', to='bake.User'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='uploaded_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes_uploaded', to='bake.User'),
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messages', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('recipe_message', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recipe_message', to='bake.Recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_name', models.CharField(max_length=255)),
                ('ingredient_quantity', models.FloatField(null=True)),
                ('ingredient_measurement', models.CharField(max_length=15, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ingredients_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_ingredients', to='bake.Recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_image', models.ImageField(upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='for_recipe', to='bake.Recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('mess_comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recipe_comment', to='bake.Messages')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('categories', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recipe_categories', to='bake.Recipe')),
            ],
        ),
    ]
