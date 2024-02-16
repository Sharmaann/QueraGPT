from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from .models import Question, Answer
from .forms import QuestionForm


def get_question_title(request):
    if request.method == "GET":
        question_id = request.GET.get("question_id")
        try:
            question = Question.objects.get(id=question_id)
            return HttpResponse(f"Title: {question.title}")
        except:
            return HttpResponse("Question not found")
    return HttpResponse("Method not allowed")


@csrf_exempt
def add_question(request):
    if request.method == "POST":
        form = QuestionForm()
        context = {"question_form": form}
        return render(request, "question_add.html", context)

    return HttpResponse("Method not allowed")
