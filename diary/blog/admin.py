from django.contrib import admin
from .models import Post, PostImages

#admin.site.register(Post)
#admin.site.register(PostImages)

class PostImagesInline(admin.TabularInline):
    model = PostImages
    extra = 0

# class PostImagesAdmin(admin.ModelAdmin):
#     list_display = ('post', 'image', 'order')

def first_50_symbols_text(obj):
    return ("%s" % (obj.text))[:50]
first_50_symbols_text.short_description = 'Text'



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',first_50_symbols_text, 'post_date', 'modify_date', 'status')
    inlines = [PostImagesInline]

@admin.register(PostImages)
class PostImagesAdmin(admin.ModelAdmin):
    list_display = ('post', 'image', 'order')