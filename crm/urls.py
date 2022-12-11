from django.urls import path
from .views import *

urlpatterns = [
    path('', all_students, name='all_students'),
    path('add_student/', add_student, name='add_student'),
]
