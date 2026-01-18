from django.urls import path
from .views import (
    CoursesEditView, CoursesListCreateView, ModulListCreateView, ModulEditView,
    TaskCreateListView, TaskEditView, SubmissionView
)

urlpatterns = [
    path('', TaskCreateListView.as_view(), name='task_list_create'),
    path('submission/', SubmissionView.as_view(), name='submission'),
    path('task/', TaskCreateListView.as_view()),
    path('course/', CoursesListCreateView.as_view(), name='courses_list_create'),
    path('module/', ModulListCreateView.as_view(), name='module_list_create'),

    path('task/edit/task_id/', TaskEditView.as_view(), name='edit_task'),
    path('course/edit/course_id/', CoursesEditView.as_view(), name='course_edit'),
    path('modul/edit/modul_id/', ModulEditView.as_view(), name='modul_edit')
]
