from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^data$',views.data,name='data'),
    url(r'^bin1$',views.bin1,name='bin1'),
    url(r'^maps$',views.maps,name='maps'),
    url(r'^bin2$',views.bin2,name='bin2'),
    url(r'^bin3$',views.bin3,name='bin3'),
    url(r'^google$',views.google,name='google'),
    url(r'^graphs$',views.graphs,name='graphs'),
]
