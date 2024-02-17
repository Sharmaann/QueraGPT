from django.contrib import admin
from .models import Question, Answer, Problem

# Register your models here.


class ProblemInline(admin.StackedInline):
    model = Problem


class QuestionInline(admin.StackedInline):
    model = Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
