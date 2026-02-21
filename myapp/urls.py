from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('hello/<str:username>', views.hello, name='hello'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:id>', views.project_detail, name='project_detail'),
    path('tasks/', views.tasks, name='tasks'),
    path('create_task/', views.create_task, name='create_task'),
    path('delete_task/<int:id>/', views.delete_task, name='delete_task'),
    # path('edit_task/', views.edit_task, name='edit_task'),
    path('edit_task/<int:id>/', views.edit_task, name='edit_task'),
    path('toggle_task/<int:id>/', views.toggle_task, name='toggle_task'),
    path('create_project/', views.create_project, name='create_project'),
]