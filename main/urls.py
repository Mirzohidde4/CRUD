from django.urls import path
from .views import ( 
    Home, 
    Shop, 
    Detail, 
    Create, 
    Edit, 
    Delete,
    MyPosts,
)

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('shop/', Shop.as_view(), name='shop'),
    path('myposts/', MyPosts.as_view(), name='myposts'),
    path('post/<int:pk>/', Detail.as_view(), name='detail'),
    path('post/new/', Create.as_view(), name='newpost'),
    path('post/edit/<int:pk>/', Edit.as_view(), name='postedit'),
    path('post/delete/<int:pk>/', Delete.as_view(), name='postdelete'),
]