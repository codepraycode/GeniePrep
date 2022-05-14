from django.urls import path
from .views import LogInView, UsersView, UserView

urlpatterns = [
    path('', view=UsersView.as_view(), name="index"),
    path('login', view=LogInView.as_view(), name="login"),
    path('data', view=UserView.as_view(), name="data"),
]
