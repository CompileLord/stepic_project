from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = 'ST', 'Student'
        MENTOR = 'MN', 'Mentor'

    role = models.CharField(
        choices=Role.choices,
        default=Role.STUDENT,
    )

    REQUIRED_FIELDS = []

