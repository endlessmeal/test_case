from django.db import models


class Survey(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Name", max_length=255)
    date_created = models.DateTimeField("Date Created")
    date_ended = models.DateTimeField("Date ended")
    description = models.CharField("Description", max_length=255)

    def __str__(self):
        return str(self.id)


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    TYPE_QUESTION_TEXT = 'Text'
    TYPE_QUESTION_CHOICE = 'Choice'
    TYPE_QUESTION_MULTIPLE_CHOICE = 'Multiple Choice'

    QUESTION_TYPE = (
        (TYPE_QUESTION_TEXT, "Text"),
        (TYPE_QUESTION_CHOICE, "Choice"),
        (TYPE_QUESTION_MULTIPLE_CHOICE, "Multiple Choice"),
    )

    survey = models.ForeignKey(Survey, null=True, related_name="survey", on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    type_question = models.CharField(max_length=255, choices=QUESTION_TYPE, default=TYPE_QUESTION_TEXT)
    body = models.CharField(max_length=512, default='This is a text question')

    def __str__(self):
        return self.title






