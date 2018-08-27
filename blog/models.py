from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 250)
    date_posted = models.DateTimeField()
    body = RichTextUploadingField()
    # image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title

    def summary(self):
        if (len(self.body) > 300):
            return self.body[:300] + " [...]"
        else:
            return self.body

    def date_modified(self):
        return self.date_posted.strftime('%b %e %Y')