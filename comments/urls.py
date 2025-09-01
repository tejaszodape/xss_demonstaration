from django.urls import path
from . import views

app_name = 'comments'

urlpatterns = [
    path('', views.xss_demo, name='xss_demo'),
]