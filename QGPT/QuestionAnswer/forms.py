from django import forms

from .models import Question, Answer, Problem


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = "__all__"


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = "__all__"
        
class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = "__all__"
