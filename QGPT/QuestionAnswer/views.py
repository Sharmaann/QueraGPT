from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from .models import Question, Answer, Problem
from .forms import QuestionForm, AnswerForm, ProblemForm


def get_question_title(request):  # TODO
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
    if request.method == "GET":
        form = QuestionForm()
        context = {"form": form}
        return render(request, "add_form.html", context)

    if request.method == "POST":  # TODO
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            Question.objects.create(**data)
            return HttpResponse("Question added", status=201)
        return HttpResponse("Error", status=400)

    return HttpResponse("Method not allowed")


# REFACTOR: code duplication


@csrf_exempt
def add_answer(request):
    if request.method == "GET":
        form = AnswerForm()
        context = {"form": form}
        return render(request, "add_form.html", context)

    if request.method == "POST":  # TODO
        form = AnswerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Question.objects.create(**data)
            return HttpResponse("Answer added", status=201)
        return HttpResponse("Error", status=400)

    return HttpResponse("Method not allowed")


@csrf_exempt
def add_problem(request):
    if request.method == "GET":
        form = ProblemForm()
        context = {"form": form}
        return render(request, "add_form.html", context)

    if request.method == "POST":  # TODO
        form = ProblemForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Problem.objects.create(**data)
            return HttpResponse("Problem added", status=201)
        return HttpResponse("Error", status=400)

    return HttpResponse("Method not allowed")
