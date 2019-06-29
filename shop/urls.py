from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index, name="index"),
    path('cart',views.cart, name="cart"),
    path('categories',views.categories, name="categories"),
    path('checkout',views.checkout, name="checkout"),
    path('contact',views.contact, name="contact"),
    path('product/<int:pk>/',views.product, name="product"),
    path('allproducts/<int:pk>/', views.allproducts, name="allproduct"),
    ]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)