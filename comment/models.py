from django.db import models
from video.models import Video 

class Comment(models.Model):
	author = models.ForeignKey(
		'auth.User',
        on_delete=models.CASCADE,
		)

	content = models.TextField()
	video = models.ForeignKey(
		Video,
		on_delete=models.CASCADE,
		)

	def __str__(self):
		return "comment" + str(self.id)