from django.urls import path
from app import views
urlpatterns = [
    path('', views.postList, name='postList'),
    path('postDetail/<int:pk>/', views.postDetail, name='postDetail'),
    path('postDelete/<int:pk>/', views.postDelete, name='postDelete'),
    path('postUpdate/<int:pk>/', views.postUpdate, name='postUpdate'),
]
