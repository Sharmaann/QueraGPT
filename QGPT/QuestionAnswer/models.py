from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models


from .validators import FileSizeValidator

ONE_MEGABYTE = 1048576


def image_directory(instance, filename):
    return "media/user_{}/{}".format(instance.user.username, filename)


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
        upload_to=image_directory,
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"]),
            FileSizeValidator(2 * ONE_MEGABYTE),
        ],
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
