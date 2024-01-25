from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('word_detail/<str:word>/', views.word_detail, name='word_detail'),
    path('search/', views.search_results, name='search_results'),
    path('<str:word>/', views.word_detail, name='word_detail'),
    
]