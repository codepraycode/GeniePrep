from django.urls import path
from .views import index

app_name = "frontend"


urlpatterns = [
    path('', view=index, name=''),
    path('signin', view=index, name='sigin'),
    path('signup', view=index, name='signup'),
    
    path('dashboard', view=index, name='dashboard'),
]
