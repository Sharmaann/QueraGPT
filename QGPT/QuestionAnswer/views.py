from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


from .forms import QuestionForm, AnswerForm, ProblemForm
from .models import Question, Answer, Problem
from openAI_API import chat_gpt_answer


# REFACTOR: code logic duplication


def get_question(request):
    if request.method == "GET":
        question_id = request.GET.get("question_id")
        if question_id is None:
            return HttpResponse("Please give question_id query param")

        try:
            question_obj = Question.objects.get(pk=question_id)
            q_title = question_obj.title
            q_user = question_obj.user.username
            q_text = question_obj.question_text
            message = f"""
                        title: {q_title}<br>
                        username: {q_user}<br>
                        text: {q_text}<br>
                    """

            return HttpResponse(message)
        except:
            return HttpResponse("Question doesn't exist")
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


def get_answer(request):
    if request.method == "GET":
        answer_id = request.GET.get("answer_id")
        if answer_id is None:
            return HttpResponse("Please give answer_id query param")

        try:
            answer_obj = Answer.objects.get(pk=answer_id)
            answer_text = answer_obj.answer_text
            return HttpResponse(f"Answer text: {answer_text}")
        except:
            return HttpResponse("Answer doesn't exist")
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


def get_problem(request):
    if request.method == "GET":
        problem_id = request.GET.get("problem_id")
        if problem_id is None:
            return HttpResponse("Please give problem_id query param")

        try:
            problem_obj = Problem.objects.get(pk=problem_id)
            problem_name = problem_obj.name
            return HttpResponse(f"Problem name: {problem_name}")
        except:
            return HttpResponse("Problem doesn't exist")
    return HttpResponse("Method not allowed")


def AI_answer(request):
    if request.method == "GET":
        question_id = request.GET.get("question_id")
        if question_id is None:
            return HttpResponse("Please give question_id query param")
        try:
            question_obj = Question.objects.get(pk=question_id)
            q_text = question_obj.question_text
            answer_text = chat_gpt_answer(q_text)
            message = f"GPT answer: {answer_text}"
            Answer.objects.create(question=question_obj, answer_text=answer_text)
            return HttpResponse(message)
        except:
            return HttpResponse("Question doesn't exist")

    return HttpResponse("Method not allowed")


def mentor_answer(request):
    if request.method == "POST":
        question_id = request.GET.get("question_id")
        if question_id is None:
            return HttpResponse("Please give question_id query param")
        try:
            question_obj = Question.objects.get(pk=question_id)
            q_text = question_obj.question_text
            answer_text = "Mentor's answer"  # should have form, responder_id (but I don't have time :))
            message = f"GPT answer: {answer_text}"
            responder_id = 1
            responder_obj = User.objects.get(pk=responder_id)
            Answer.objects.create(
                responder=responder_obj,
                question=question_obj,
                answer_text=answer_text,
                gpt_used=False,
            )
            return HttpResponse(message)
        except:
            return HttpResponse("Question doesn't exist")

    return HttpResponse("Method not allowed")
