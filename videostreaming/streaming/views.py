from django.shortcuts import render , redirect, get_object_or_404
from django.http import HttpResponse
from .forms import VideoForm
from .models import Video
# Create your views here.

def index(request):
    return HttpResponse("ye Dekho mai doobara aa gaya.")

def upload_video(request):
    if request.method=='POST':
        form = VideoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm()
        return render(request,'upload_video.html',{'form':form})    
        

def video_list(request):
    videos =Video.objects.all()
    return render(request,'video_list.html',{'videos':videos})

def video_detail(request,pk):
    video = get_object_or_404(Video,pk=pk)
    return render(request,'video_detail.html',{'video':video})
        