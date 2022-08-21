from django.db import models

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    lesson_text = models.TextField()

# class Snippet(models.Model):
#     text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ('-created_at', )