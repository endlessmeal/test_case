from rest_framework import serializers
from surveys.models import Survey, Question
from users.models import Answer
import logging


class SurveyListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Survey
        fields = ['id', 'name', 'date_created', 'date_ended', 'description']


class QuestionsListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'title', 'type_question']


class CreateAnswerSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        context = kwargs.get('context', None)
        if context:
            request = kwargs['context']['request']

            pk = request.GET.get('pk')
            logging.debug(pk)
            if pk:
                self.fields['question'] = Question.objects.filter(survey_id=pk)

    class Meta:
        model = Answer
        fields = ['question', 'body']





