from django.urls import path
from . import views

urlpatterns = [
    path('persons/', views.persons_list, name='persons_list'),
]
