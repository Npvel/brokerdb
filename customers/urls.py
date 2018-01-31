from django.conf.urls import url
from . import views

urlpatterns = [
    
    url(r'^csvupload$', views.csvupload, name='csvupload'),
]