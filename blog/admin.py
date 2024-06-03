from django.contrib import admin
from .models import Post, Category, Tag, Gallery, Author, About, Pricing, In_Touch


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    filter_horizontal = ('tags',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Gallery)
admin.site.register(Author)
admin.site.register(About)
admin.site.register(Pricing)
admin.site.register(In_Touch)
