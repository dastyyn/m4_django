# Generated by Django 5.0.2 on 2024-02-20 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cook_book', '0002_alter_recipes_options_reviesrecipes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ReviesRecipes',
            new_name='ReviewsRecipes',
        ),
    ]
