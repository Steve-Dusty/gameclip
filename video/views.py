from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Video


def index(request):
    videos = Video.objects.all()
    context = {'videos': videos}
    return render(request, 'index.html', context=context)


@login_required(login_url='/accounts/login/')
def upload_video(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        video = request.FILES['video_file']
        unlisted = request.POST.get('unlisted', False)
        creator = request.user
        video = Video(title=title, description=description, video_file=video, unlisted=unlisted, creator=creator)
        video.save()

    return render(request, 'upload.html')


@login_required(login_url='/accounts/login/')
def dashboard(request):
    videos = Video.objects.all().filter(
        creator=request.user
    )
    context = {'videos': videos}
    return render(request, 'dashboard.html', context=context)


def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    context = {"video": video}
    return render(request, 'video.html', context=context)
