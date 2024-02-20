from django import forms
from . import models


class CookBookForm(forms.ModelForm):
    class Meta:
        model = models.Recipes
        fields = "__all__"
