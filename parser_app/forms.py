from django import forms
from . import parser, models


class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ("FOOD.ru", 'FOOD.ru'),
    )

    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = ('media_type',)

    def parser_data(self):
        if self.data['media_type'] == 'FOOD.ru':
            food_parser = parser.parsing()
            for i in food_parser:
                models.ParsingFood.objects.create(**i)


