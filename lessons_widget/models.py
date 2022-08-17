from django.db import models

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    lesson_text = models.TextField()
