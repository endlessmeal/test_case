from django.db import models
from surveys.models import Question


class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    body = models.CharField(max_length=512)
