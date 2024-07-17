from django.urls import path
from .views import SignPage, LoginPage, LogoutPage


urlpatterns = [
    path('login', LoginPage, name='login'),
    path('sign', SignPage, name='sign'),
    path('logout', LogoutPage, name='logout'),
]