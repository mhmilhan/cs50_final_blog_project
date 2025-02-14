from django.contrib import admin
from .models import Category, SocialMediaLink, Blog

# Register your models here.
class SocialMediaLinkAdmin(admin.ModelAdmin):
    list_display = ['platform', 'url']

class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ['author']  # Make the author field read-only during editing


    def save_model(self, request, obj, form, change):
        if not change or not obj.author:  # If it's a new post (not being edited), set the author
            obj.author = request.user
        super().save_model(request, obj, form, change)

    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'author', 'category', 'is_featured', 'is_approved', 'published_at']
    search_fields = ['title', 'author', 'category']
    list_filter = ['category', 'is_featured', 'is_approved']
    list_editable = ['is_featured', 'is_approved']    

admin.site.register(SocialMediaLink)
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)   
