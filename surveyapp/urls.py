from django.urls import path
from surveys import views
from users.views import SurveyListView, QuestionsOfSurveyListView, CreateAnswerView


urlpatterns = [
    path('api/surveys/create', views.SurveyCreateView.as_view(), name='Create Survey'),
    path('api/surveys/update_delete/<int:pk>/', views.SurveyDetailView.as_view(), name='Update or delete Survey'),
    path('api/surveys/question/create', views.QuestionCreateView.as_view(), name='Create question'),
    path('api/surveys/question/update_delete/<int:pk>/', views.QuestionDetailView.as_view(), name='Update or delete Question'),

    path('api/users/all_surveys', SurveyListView.as_view(), name='List of all Surveys'),
    path('api/users/survey/questions/<int:pk>/', QuestionsOfSurveyListView.as_view(), name='List of all question in Survey'),
    path('api/users/survey/questions/answer/<int:pk>/', CreateAnswerView.as_view(), name='Create an answer')
]