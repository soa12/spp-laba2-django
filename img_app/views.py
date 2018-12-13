from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Image

def image_list(request):
    images_list = Image.objects.all()
    paginator = Paginator(images_list, 8)
    page = request.GET.get('page') 
    images = paginator.get_page(page)
    return render(request, 'img_app/image_list.html', {'images': images})

def detail(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    return render(request, 'img_app/image_detail.html', {'image': image})

def vote(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    if 'dislike' in request.path:
        image.dislikes += 1
    elif 'like' in request.path:
        image.likes += 1
    image.save()
    return redirect(image_list)

def statistics(request):
    images = Image.objects.all()
    return render(request, 'img_app/statistics.html', {'images': images})

