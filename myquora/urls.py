from django.urls import path
from . import views

app_name = 'myquora'

urlpatterns = [
    path('', views.home, name='home'),
    path('questions/', views.question_list, name='questions-list'),
    path('question/<str:slug>/', views.question_detail, name='question-detail'),
    path('question/<str:slug>/', views.question_detail, name='question-detail'),
    # path('category/<int:category_id>/<str:category_slug>/questions/', views.category_questions, name='category-questions'),
]