from rest_framework import serializers
from .models import Courses, Modul, Task, OutputInput, Submission

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['id', 'title', 'description', 'mentor', 'created_at', 'updated_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['mentor'] = instance.mentor.username
        return representation

class ModulSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modul
        fields = ['id', 'title', 'description', 'course']
    

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'text', 'modul', 'created_at']


class OutputInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutputInput
        fields = ['id', 'output', 'input', 'task']

class Submission(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['id', 'user', 'task', 'code', 'created_at', 'updated_at', 'is_correct']
    
    