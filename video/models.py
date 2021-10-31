from django.core.files.storage import FileSystemStorage
from django.db import models


class Video(models.Model):
    video_file = models.FileField(upload_to='videos/')
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, default="No Description")
    unlisted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title