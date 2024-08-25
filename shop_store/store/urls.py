from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('store/', views.store, name='store'),
    path('store/details/<str:category>/<int:id>/', views.detail, name= 'detail'),
    path('store/cart/', views.cart, name= 'cart'),
    path('store/account/', views.account, name= 'account'),
    path('store/contact/', views.contact, name= 'contact'),
    path('store/login/', views.login, name= 'login'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)