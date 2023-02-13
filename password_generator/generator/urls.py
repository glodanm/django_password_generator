from django.urls import path
from .views import home, password, about

urlpatterns = [
    path('', home, name='home'),
    path('generated_password/', password, name='password'),
    path('about/', about, name='about'),
]