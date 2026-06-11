from django.urls import path
from . import views

urlpatterns = [
    path('', views.author_list, name='author_list'),
    path('create/', views.create_author, name='create_author'), # <--- ДОДАЙ ЦЕЙ РЯДОК
]