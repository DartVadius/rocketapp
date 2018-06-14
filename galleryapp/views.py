from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import permission_required
from galleryapp.models import Photo, Gallery, Tag
from django.core.paginator import Paginator


def index(request):
    gallery_list = Gallery.objects.order_by('-created_at').all()
    paginator = Paginator(gallery_list, 12)
    page = request.GET.get('page')
    galleries = paginator.get_page(page)
    return render(
        request,
        'gallery_index.html',
        context={'galleries': galleries},
    )


def gallery(request, gallery_slug):
    gallery_item = get_object_or_404(Gallery, slug=gallery_slug)
    return render(
        request,
        'gallery_page.html',
        context={
            'gallery': gallery_item,
            'Title': gallery_item.meta_title,
            'description': gallery_item.meta_description,
            'keywords': gallery_item.meta_keywords
        },
    )


def tag(request, gallery_tag):
    blog_tag = get_object_or_404(Tag, name=gallery_tag)
    gallery_list = Gallery.objects.order_by('-created_at').filter(tag=blog_tag).all()
    paginator = Paginator(gallery_list, 15)
    page = request.GET.get('page')
    galleries = paginator.get_page(page)
    return render(
        request,
        'gallery_index.html',
        context={
            'galleries': galleries,
        },
    )


@permission_required('True', raise_exception=True)
def delete_photo(request, photo_id):
    Photo.objects.get(id=photo_id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))