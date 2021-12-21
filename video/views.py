from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Video


def index(request):
    videos = Video.objects.all().order_by('-id')
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
        clip = Video(title=title, description=description, video_file=video, unlisted=unlisted, creator=creator)
        if video.size > 524288000:
            return redirect('upload_video')
        else:
            clip.save()
            return redirect('index')
    return render(request, 'upload.html')


@login_required(login_url='/accounts/login/')
def dashboard(request):
    videos = Video.objects.all().filter(
        creator=request.user
    )
    context = {'videos': videos}
    return render(request, 'dashboard.html', context=context)

@login_required(login_url='/accounts/login/')
def delete_video(request, pk):
    video = Video.objects.get(id=pk)
    video.delete()
    return redirect('dashboard')

def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    context = {"video": video}
    return render(request, 'video.html', context=context)
