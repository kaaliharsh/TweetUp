from .import views
from django.urls import path


urlpatterns=[
    path('', views.tweet_list, name='tweet_list'),
    path('create/', views.tweet_create, name='tweet_create'),
    path('<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),
    path('<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),
    path('register/', views.register, name='register'),
    path('search/', views.search_view, name='search'),
    path('', views.tweet_list, name='tweet_list'),
    path('tweet/<int:tweet_id>/', views.tweet_detail, name='tweet_detail'),
    path('search/', views.search_view, name='search'),
    path('follow/<str:username>/', views.follow_unfollow, name='follow_unfollow'),
    
    
   
]