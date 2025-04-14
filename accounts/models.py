from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('secondary_student', 'Secondary Student'),
        ('tertiary_student', 'Tertiary Student'),
        ('adult', 'Adult'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
