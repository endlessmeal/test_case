from rest_framework import generics
from surveys.models import Survey, Question
from users.serializers import (
    SurveyListSerializer,
    QuestionsListSerializer,
    CreateAnswerSerializer,
)


class SurveyListView(generics.ListAPIView):
    serializer_class = SurveyListSerializer
    queryset = Survey.objects.all()


class QuestionsOfSurveyListView(generics.ListAPIView):
    serializer_class = QuestionsListSerializer

    def get_queryset(self):
        queryset = Question.objects.filter(survey_id=self.kwargs['pk'])
        return queryset


class CreateAnswerView(generics.CreateAPIView):
    serializer_class = CreateAnswerSerializer

