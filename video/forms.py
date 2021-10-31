from django import forms
from .models import Video

class UploadVideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'video_file', 'unlisted']