from django.shortcuts import render
from blog.models import Category, SocialMediaLink, Blog

def index(request):
    categories = Category.objects.all()
    social_media_links = SocialMediaLink.objects.all()
    category_posts = {
    category.category_name: category.blog_set.all()[:4]  # Fetch 4 posts per category
    for category in categories
    }
    featured_post_list = Blog.objects.filter(is_featured=True)[:5] 
    context = {
        'categories': categories,
        'featured_post_list': featured_post_list,
        'social_media_links': social_media_links,
    }

    return render(request, 'blog/homepage.html', context)