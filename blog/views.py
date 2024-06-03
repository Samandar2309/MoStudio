from django.shortcuts import render
from .models import Post, Author, Gallery, Pricing, Contact, In_Touch, About


# Create your views here.

def home_view(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'index.html', context)


def gallery_view(request):
    gallery = Gallery.objects.all()
    context = {'gallery': gallery}
    return render(request, 'gallery.html', context)


def about_view(request):
    about = About.objects.all()
    authors = Author.objects.all()
    context = {'about': about,
               'authors': authors}
    return render(request, 'about.html', context)


def pricing_view(request):
    pricing = Pricing.objects.all()
    context = {'pricing': pricing}
    return render(request, 'pricing.html', context)


def in_touch_view(request):
    in_touch = In_Touch.objects.all()
    contact = Contact.objects.all()
    context = {'in_touch': in_touch, 'contact': contact}
    return render(request, 'contact.html', context)
