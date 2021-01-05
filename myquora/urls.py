from django.urls import path
from . import views

app_name = 'myquora'

urlpatterns = [
    path('', views.home, name='home'),
    path('listquestions/', views.question_list, name='question-list'),
    path('questions/<int:pk>/',views.QuestionDetailView.as_view(), name="question-detail"),
    path('category/<str:slug>/question/', views.category_questions, name='category-questions'),
    path('insert/', views.add_question, name='add-question'),
    path('like/<int:pk>/', views.like_view, name="question_like"),
    path("create/<str:pk>", views.create_answer, name="create-answer"),
    path("my_question/", views.MyQuestionList.as_view(), name="my-question"),
    # path("update_question/<str:pk>", views.update_question, name="update-question"),
    # path("delete_question/<str:pk>", views.delete_question, name="delete-question"),

]

