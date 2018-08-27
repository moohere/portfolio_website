from django.db import models

# Create your models here.
class Project(models.Model):
    summary = models.CharField(max_length=200)
    img = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.summary