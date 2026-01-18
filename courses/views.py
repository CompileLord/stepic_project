from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .helpers import check_and_run_command
from .models import Courses, Modul, Task, OutputInput, Submission
from .serializers import CoursesSerializer, ModulSerializer, TaskSerializer




class CoursesListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        courses = Courses.objects.all()
        serializer = CoursesSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=CoursesSerializer,
        operation_description="Create a task using a form instead of JSON"
    )
    def post(self, request):
        serializer = CoursesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CoursesEditView(APIView):
    permission_classes = [permissions.IsAdminUser]

    @swagger_auto_schema(
        request_body=CoursesSerializer,
        operation_description="Create a task using a form instead of JSON"
    )
    def put(self, request, course_id):
        course = Courses.objects.get(id=course_id)
        serializer = CoursesSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=CoursesSerializer,
        operation_description="Create a task using a form instead of JSON"
    )
    def patch(self, request, course_id):
        course = Courses.objects.get(id=course_id)
        serializer = CoursesSerializer(course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, course_id):
        course = Courses.objects.filter(id=course_id)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class ModulListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        moduls = Modul.objects.all()
        serializer = ModulSerializer(moduls, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        request_body=ModulSerializer,
        operation_description="Create a task using a form instead of JSON"
    )
    def post(self, request):
        serializer = ModulSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ModulEditView(APIView):
    permission_classes = [permissions.IsAdminUser]

    @swagger_auto_schema(
        request_body=ModulSerializer,
        operation_description="Create a task using a form instead of JSON"
    )
    def put(self, request, modul_id):
        modul = Modul.objects.filter(id=modul_id)
        serializer = ModulSerializer(modul, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        request_body=ModulSerializer,
        operation_description="Create a task using a form instead of JSON"
    )
    def patch(self, request, modul_id):
        modul = Modul.objects.filter(id=modul_id)
        serializer = ModulSerializer(modul, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, modul_id):
        modul = Modul.objects.filter(id=modul_id)
        modul.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TaskCreateListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        request_body=TaskSerializer,
        operation_description="Create a task using a form instead of JSON"
    )
    
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskEditView(APIView):
    permission_classes = [permissions.IsAdminUser]

    @swagger_auto_schema(
        request_body=TaskSerializer,
        operation_description="Create a task using a form instead of JSON"
    )
    def put(self, request, task_id):
        taks = Task.objects.filter(id=task_id)
        serializer = TaskSerializer(taks, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        request_body=TaskSerializer,
        operation_description="Create a task using a form instead of JSON"
    )
    def patch(self, request, taks_id):
        task = Task.objects.filter(id=taks_id)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, taks_id):
        task = Task.objects.filter(id=taks_id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class SubmissionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Submit python code to be checked",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['code'],
            properties={
                'code': openapi.Schema(
                    type=openapi.TYPE_STRING, 
                    description="Paste your Python code here"
                ),
            }
        ),
    )
    def post(self, request, task_id):
        user_code = request.data.get('code')
        result_message = check_and_run_command(user_code, task_id)
        
        status_choice = Submission.IsCorrect.CORRECT if result_message == "Correct" else Submission.IsCorrect.INCORRECT
        
        Submission.objects.create(
            user=request.user,
            task_id=task_id,
            code=user_code,
            is_correct=status_choice
        )
        
        return Response({"result": result_message}, status=status.HTTP_200_OK)
    


    
