from django.views import generic
from . import models


class ProductListView(generic.ListView):
    template_name = 'product/product_list.html'
    context_object_name = 'all_products'
    model = models.Product

    def get_queryset(self):
        tag_id = self.request.GET.get('tag')
        if tag_id:
            return self.model.objects.filter(tag__id=tag_id).order_by('-id')
        else:
            return self.model.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_tags'] = models.Tag.objects.all()
        return context


class ManClothesView(generic.ListView):
    template_name = 'product/men_products.html'
    context_object_name = 'men_products'
    model = models.Product

    def get_queryset(self):
        return self.model.objects.filter(tag__name='Мужское').order_by('-id')


class GirlClothesView(generic.ListView):
    template_name = 'product/girl_products.html'
    context_object_name = 'girl_products'
    model = models.Product

    def get_queryset(self):
        return self.model.objects.filter(tag__name='Женское').order_by('-id')



class KidClothesView(generic.ListView):
    template_name = 'product/Kid_products.html'
    context_object_name = 'Kid_products'
    model = models.Product

    def get_queryset(self):
        return self.model.objects.filter(tag__name='Детское').order_by('-id')


