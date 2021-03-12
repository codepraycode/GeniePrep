from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('register', views.register, name="register"),
    path('logout', views.logout, name="logout"),

    
    path('dashboard', views.dashview, name="dashboard"),
    path("profile", views.profile, name="profile"),
    path("leaderboard", views.leaderBoard, name="leaderboard"),
    path("records", views.records, name="records"),
    
    
]
