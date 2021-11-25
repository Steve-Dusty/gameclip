from django.core.files.storage import FileSystemStorage
from django.db import models
from django.urls import reverse


class Video(models.Model):
    video_file = models.FileField(upload_to='videos/')
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, default="No Description")
    unlisted = models.BooleanField(default=False)
    creator = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

