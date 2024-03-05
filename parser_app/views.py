from django.http import HttpResponse
from django.views import generic
from . import models, parser, forms


class ParserListFood(generic.ListView):
    model = models.ParsingFood
    template_name = 'parser/food_list.html'
    context_object_name = 'food'

    def get_queryset(self):
        return models.ParsingFood.objects.all()


class GetParsingForm(generic.FormView):
    template_name = 'parser/food_form.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('<h1>Parsing... </h1><a href="/food_list/">Перейти к блюдам</a>')
        else: super(GetParsingForm, self).post(request, *args, **kwargs)
