from django.db import models

# Create your models here.

class Task(models.Model):
    # An ID field is automatically added to all Django models
    description = models.CharField(max_length=255)
    # This Boolean field is used to mark a task as completed
    completed = models.BooleanField(default=False)
