from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data/', views.data, name='data'),
    path('bin1/', views.bin1, name='bin1'),
    path('maps/', views.maps, name='maps'),
    path('bin2/', views.bin2, name='bin2'),
    path('bin3/', views.bin3, name='bin3'),
    path('google/', views.google, name='google'),
    path('graphs/', views.graphs, name='graphs'),
]
