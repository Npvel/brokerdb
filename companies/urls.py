from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.find_company, name='find_company'),
    url(r'^multiple$', views.list_of_companies, name='list_of_companies'),
]