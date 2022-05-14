from django.urls import path
from .views import QuestionView, SubmitView

urlpatterns = [
    path('questions', view=QuestionView.as_view(), name="question"),
    path('submit', view=SubmitView.as_view(), name="submit"),
]
