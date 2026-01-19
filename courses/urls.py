from django.urls import path
from .views import (
    CoursesEditView, CoursesListCreateView, ModulListCreateView, ModulEditView,
    TaskCreateListView, TaskEditView, SubmissionView, OutputInputListCreate, OutputInputEditView
)

urlpatterns = [
    path('', TaskCreateListView.as_view(), name='task_list_create'),
    path('submission/<int:task_id>/', SubmissionView.as_view(), name='submission'),
    path('task/', TaskCreateListView.as_view()),
    path('course/', CoursesListCreateView.as_view(), name='courses_list_create'),
    path('module/', ModulListCreateView.as_view(), name='module_list_create'),
    path('outout_input/', OutputInputListCreate.as_view(), name='output_input'),
    
    path('task/edit/<int:task_id>/', TaskEditView.as_view(), name='edit_task'),
    path('course/edit/<int:course_id>/', CoursesEditView.as_view(), name='course_edit'),
    path('modul/edit/<int:modul_id>/', ModulEditView.as_view(), name='modul_edit'),
    path('output_input/edit/<int:output_id>/', OutputInputEditView.as_view(), name='output_input_edit'),
]