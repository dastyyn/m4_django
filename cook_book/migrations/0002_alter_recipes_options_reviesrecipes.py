# Generated by Django 5.0.2 on 2024-02-20 13:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cook_book', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipes',
            options={'verbose_name': 'Рецепт', 'verbose_name_plural': 'Рецепты'},
        ),
        migrations.CreateModel(
            name='ReviesRecipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Напишите комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('recipe_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_recipes', to='cook_book.recipes')),
            ],
        ),
    ]