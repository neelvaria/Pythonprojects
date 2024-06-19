from django.shortcuts import render , redirect
import uuid
from .models import url
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def shorten(request):
    if request.method == 'POST':
        original_url = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = url(link=original_url, uuid=uid)
        new_url.save()
        return HttpResponse(uid)
    return render(request, 'index.html')

def go(request, pk):
    url_details = url.objects.get(uuid=pk)
    return redirect('https://'+url_details.link)
