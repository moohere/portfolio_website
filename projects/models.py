from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Project(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    summary = models.CharField(max_length=250)

    def __str__(self):
        return self.summary