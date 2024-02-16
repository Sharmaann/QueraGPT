from django.urls import path

from .views import get_question_title, add_question

urlpatterns = [
    path('question/add/', add_question),
    path('question/title/', get_question_title)
]