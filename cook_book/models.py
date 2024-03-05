from django.db import models


class Recipes(models.Model):
    DIFFICULTY_CHOICES = (
        ('easy', 'Легкий'),
        ('medium', 'Средний'),
        ('hard', 'Сложный'),
    )
    title = models.CharField(max_length=50, verbose_name='Название блюда:')
    description = models.TextField(verbose_name='Описание блюда:')
    ingredients = models.TextField(verbose_name='Ингредиенты:')
    steps = models.TextField(verbose_name='Последовательность приготовления:')
    price = models.PositiveIntegerField(verbose_name='Примерная стоимость:')
    image = models.URLField(verbose_name='Ссылка на изображение:')
    time_cook = models.PositiveIntegerField(verbose_name='Время готовки:')
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES,
                                default='easy', verbose_name='Сложность приготовления', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} ({self.difficulty})'

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
