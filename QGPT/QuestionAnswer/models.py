from django.db import models

ONE_MEGABYTE = 1048576

from .validators import FileSizeValidator


class Problem(models.Model):
    name = models.CharField(max_length=15)


class Question(models.Model):
    """
    An abstract-base-class for question
    """

    title = models.CharField(max_length=20)

    # add fake data #TODO
    problem = models.OneToOneField(Problem, on_delete=models.CASCADE)

    # set max size and content type #TODO
    attachment = models.FileField(
        blank=True,
        null=True,
        validators=[FileSizeValidator(2 * ONE_MEGABYTE)],
    )
    question_text = models.TextField()
    image = models.ImageField(
        blank=True,
        null=True,
        validators=[FileSizeValidator(2* ONE_MEGABYTE)],
    )
