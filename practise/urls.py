from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.practise, name="practise"),
    path('test', views.test, name="test"),

    path('result', views.result, name="result"),

    path('marker', views.marker, name="marker"),
    path('correction', views.correction, name="correction"),
    path('dashboard', views.dashview, name="dashboard"),
    path("profile", views.profile, name="profile"),
    path("leaderboard", views.leaderBoard, name="leaderboard"),
    path("records", views.records, name="records"),
]
