from django.db import models

# Create your models here.


class Problem(models.Model):
    name = models.CharField(max_length=15)


class Question(models.Model):
    """
    An abstract-base-class for question
    """

    title = models.CharField(max_length=20)

    # add fake data #TODO
    problem = models.OneToOneField(Problem, on_delete=models.CASCADE)

    #BUG
    # set max size and content type #TODO
    attachment = models.FileField(
        blank=True, null=True, validators=[file_size_validator]
    )  # TODO
    question_text = models.TextField()
    image = models.ImageField(
        blank=True, null=True, validators=[file_size_validator]
    )  # TODO
