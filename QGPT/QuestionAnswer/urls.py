from django.urls import path

from .views import (
    get_question,
    add_question,
    add_answer,
    add_problem,
    get_problem,
    get_answer,
    AI_answer,
)

urlpatterns = [
    path("question/detail/", get_question),
    path("question/add/", add_question),
    path("problem/name/", get_problem),
    path("problem/add/", add_problem),
    path("answer/text/", get_answer),
    path("answer/add/", add_answer),
    path("question/answer/AI/", AI_answer),
]
