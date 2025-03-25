from django.urls import path
from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('delete/<int:task_index>/', views.delete, name='delete'),
    path('WorkingOnIt', views.edit, name='edit')
]