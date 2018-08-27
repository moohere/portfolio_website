from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 250)
    date_posted = models.DateTimeField()
    body = RichTextUploadingField()

    def __str__(self):
        return self.title

    def summary(self):
        if (len(self.body) > 100):
            return self.body[:100] + "..."
        else:
            return self.body

    def date_modified(self):
        return self.date_posted.strftime('%b %e %Y')