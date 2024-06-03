from django.urls import path
from .views import home_view, gallery_view, about_view, pricing_view, in_touch_view

urlpatterns = [
    path('', home_view, name='home'),
    path('gallery.html/', gallery_view, name='gallery'),
    path('about.html/', about_view, name='about'),
    path('pricing.html/', pricing_view, name='pricing'),
    path('contact.html/', in_touch_view, name='in_touch'),
]
