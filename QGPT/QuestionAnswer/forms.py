from django import forms

from .models import Question
from .validators import file_size_validator


class QuestionForm(forms.Form):
    class Meta:
        model = Question
        fields = "__all__"