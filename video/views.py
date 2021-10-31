from django.shortcuts import render
from .models import Video


def index(request):
    videos = Video.objects.all()
    context = {'videos': videos}
    return render(request, 'index.html', context=context)


def upload_video(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        video = request.FILES['video_file']
        unlisted = request.POST.get('unlisted', False)
        video = Video(title=title, description=description, video_file=video, unlisted=unlisted)
        video.save()
        print(video)

    return render(request, 'upload.html')
