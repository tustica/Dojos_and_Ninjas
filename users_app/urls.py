from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dojos', views.dojos_and_ninjas),
    path('process-dojo', views.process_dojo),
    path('process-ninja', views.process_ninja),
    path('process', views.process),
    path('delete-dojo', views.delete_dojo),
]