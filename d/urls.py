from django.urls import path
from . import views

app_name = 'd'

urlpatterns = [
    path('<str:word>/', views.word_detail, name='word_detail'),
]