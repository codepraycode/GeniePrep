from django.urls import path
from .views import QuestionView, TestView

urlpatterns = [
    path('questions', view=QuestionView.as_view(), name="question"),
    path('tests', view=TestView.as_view(), name="test"),
]
