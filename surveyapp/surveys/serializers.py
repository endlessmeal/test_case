from surveys.models import Survey, Question
from rest_framework import serializers


class SurveySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Survey
        fields = ['name', 'date_created', 'date_ended', 'description']


class SurveyDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Survey
        fields = ['name', 'date_ended', 'description']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['survey', 'title', 'type_question']


class QuestionDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['title', 'text']
