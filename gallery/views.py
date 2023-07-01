from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from gallery.models import Photo
from gallery.forms import PhotoForm


@login_required(login_url='/login/')
def upload_image(request):
    user = request.user
    images = Photo.objects.filter(user=user)
    context = {'images': images}

    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, user)

        if form.is_valid():
            form.instance.user = user
            form.save()
            messages.success(request, 'Image uploaded successfully.')
            return redirect('upload_image')
        else:
            messages.error(request, 'Error uploading the image.')

    else:
        form = PhotoForm(initial={'images': images})

    context['form'] = form
    return render(request, 'images.html', context)


@login_required(login_url='/login/')
def delete(request, id):
    image = get_object_or_404(Photo, id=id, user=request.user)
    image.delete()
    messages.success(request, 'Image deleted successfully.')
    return redirect(reverse('upload_image'))
