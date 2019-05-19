from django.conf.urls import url


from . import  views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^(\d+)/$',views.shiyan),
    url(r'^new1/$',views.new),
]