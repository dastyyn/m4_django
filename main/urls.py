from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from product.views import ProductListView, ManClothesView, GirlClothesView, KidClothesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book.urls')),
    path('', include('cook_book.urls')),
    path('', include('parser_app.urls')),
    path('product_list/', ProductListView.as_view(), name='product_list'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
