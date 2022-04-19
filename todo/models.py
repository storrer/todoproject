from django.db import models

# Create your models here.

class Task(models.Model):
    # An ID field is automatically added to all Django models: don't make one.
    description = models.CharField(max_length=255)
    # This Boolean field is used to mark a task as completed
    completed = models.BooleanField(default=False)

# Create a new model called Note that has one attribute called text
class Note(models.Model):
    # Only one thing in this model: a text column.
    text = models.TextField()