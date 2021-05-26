from rest_framework import generics
from surveys.serializers import (
    SurveySerializer,
    SurveyDetailSerializer,
    QuestionSerializer,
    QuestionDetailSerializer
)

from surveys.models import Survey, Question


class SurveyCreateView(generics.CreateAPIView):
    serializer_class = SurveySerializer


class SurveyDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SurveyDetailSerializer
    queryset = Survey.objects.all()


class QuestionCreateView(generics.CreateAPIView):
    serializer_class = QuestionSerializer


class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionDetailSerializer
    queryset = Question.objects.all()

