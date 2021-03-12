from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.practise, name="practise"),
    path('test', views.test, name="test"),

    path('result', views.result, name="result"),

    path('marker', views.marker, name="marker"),
    path('correction', views.correction, name="correction"),
    
]
