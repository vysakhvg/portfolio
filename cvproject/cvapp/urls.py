from django.urls import path
from cvapp import views

urlpatterns = [
    path('', views.home, name='home'),
]
