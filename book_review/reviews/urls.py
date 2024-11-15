from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/<int:pk>/add_review/', views.add_review, name='add_review'),
    path('review/<int:pk>/edit/', views.edit_review, name='edit_review'),
]
