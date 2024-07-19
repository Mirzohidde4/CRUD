from django.urls import path
from .views import SignUp, Delete, Edit


urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('delete/<int:pk>/', Delete.as_view(), name='deleteaccount'),
    path('settings/<int:pk>/', Edit.as_view(), name='settings'),
]