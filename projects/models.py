from django.db import models

# Create your models here.
class Project(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    summary = models.CharField(max_length=200)
    text = models.TextField(max_length=200, default="Text")

    def __str__(self):
        return self.summary