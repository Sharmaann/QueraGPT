from django.urls import path

from .views import get_question_title, add_question, add_answer, add_problem

urlpatterns = [
    path("question/title/", get_question_title),
    path("question/add/", add_question),
    # path('problem/name/', get_problem_name),
    path("problem/add/", add_problem),
    # path('answer/text/', get_answer_text),
    path("answer/add/", add_answer),
]
