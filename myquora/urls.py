from django.urls import path
from . import views

app_name = 'myquora'

urlpatterns = [
    path('', views.home, name='home'),
    path('listquestions/', views.question_list, name='question-list'),
    path('<str:slug>/', views.question_detail, name='question-detail'),
    path('category/<str:slug>/question/', views.category_questions, name='category-questions'),
    path('askquestion/', views.ask_question, name='askquestion')
    # path('question/<str:slug>/', views.question_detail, name='question-detail'),
    # path('add_question', views.add_question, name='add_question'),
]
