from django.urls import path
from .views import index

app_name = "frontend"


urlpatterns = [
    path('<str:apth>', view=index, name=''),
    path('<str:apth>/<str:apth1>', view=index, name=''),
    path('<str:aph1>/<str:apth>/<str:apth2>', view=index, name=''),
    # path('signin', view=index, name='sigin'),
    # path('signup', view=index, name='signup'),
    
    # path('dashboard', view=index, name='dashboard'),
    # path('result', view=index, name='result'),
    
]
