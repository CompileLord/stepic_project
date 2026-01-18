from django.urls import path
from .views import (
    CoursesEditView, CoursesListCreateView, ModulListCreateView, ModulEditView,
    TaskCreateListView, TaskEditView
)

urlpatterns = [
    path('', TaskCreateListView.as_view(), name='task_list_create'),
    path('content/tasks/', TaskCreateListView.as_view()),
    path('content/courses/', CoursesListCreateView.as_view(), name='courses_list_create'),
    path('content/modules/', ModulListCreateView.as_view(), name='module_list_create'),

    path('content/task/edit/<int:pk>/', TaskEditView.as_view(), name='edit_task'),
    path('content/courses/edit/<int:pk>/', CoursesEditView.as_view(), name='course_edit'),
    path('comnent/modul/edit/<int:pk>/', ModulEditView.as_view(), name='modul_edit')
]
