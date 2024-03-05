from django.db import models


class ParsingFood(models.Model):
    title = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    image = models.ImageField(upload_to='food/')

    def __str__(self):
        return self.title
