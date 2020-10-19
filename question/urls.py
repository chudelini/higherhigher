from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='list'),
    path('api/add-mark/', views.add_mark, name='add_mark'),
]

app_name = 'question'
