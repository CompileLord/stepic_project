from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Courses(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses_taught')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Modul(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='modules')


class Task(models.Model):
    text = models.TextField()
    modul = models.ForeignKey(Modul, on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)

class OutputInput(models.Model):
    output = models.TextField()
    input = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='output_inputs')




class Submission(models.Model):
    class IsCorrect(models.TextChoices):
        CORRECT = 'Correct'
        INCORRECT = 'Incorrect'
        REJECT = 'Reject'
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='submissions')
    code = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True )
    is_correct = models.CharField(
        choices=IsCorrect.choices,
        default=IsCorrect.REJECT,
        max_length=10
    )

    def __str__(self):
        return f"{self.user.username} - {self.task.title}"

