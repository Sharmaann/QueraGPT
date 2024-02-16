from django.db import models
from django.contrib.auth.models import User

from .validators import FileSizeValidator

ONE_MEGABYTE = 1048576


class Problem(models.Model):
    name = models.CharField(max_length=15)


class Question(models.Model):
    # get title from AI #TODO:
    title = models.CharField(max_length=20, blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # add fake data #TODO
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)

    # set content type #TODO
    attachment = models.FileField(
        blank=True,
        null=True,
        validators=[FileSizeValidator(2 * ONE_MEGABYTE)],
    )
    question_text = models.TextField()
    image = models.ImageField(
        blank=True,
        null=True,
        validators=[FileSizeValidator(2 * ONE_MEGABYTE)],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Answer(models.Model):
    # responder -> mentor -> a user
    responder = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    answer_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # responder -> chatGPT
    gpt_used = models.BooleanField(default=True)
