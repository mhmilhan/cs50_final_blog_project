from blog.models import Category,  SocialMediaLink

def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)

def get_social_media_links(request):
    social_media_links = SocialMediaLink.objects.all()
    return dict(social_media_links=social_media_links)
