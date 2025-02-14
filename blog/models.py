from django.db import models
from django_ckeditor_5.fields import CKEditor5Field 
import uuid
# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=25, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name

class SocialMediaLink(models.Model):
    PLATFORM_CHOICES = [
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
        ('instagram', 'Instagram'),
        ('youtube', 'YouTube'),
        ('whatsapp', 'WhatsApp'),
        ('telegram', 'Telegram'),
        ('discord', 'Discord'),
        ('reddit', 'Reddit'),
    ]

    platform = models.CharField(max_length=25, choices=PLATFORM_CHOICES)
    url = models.URLField(max_length=250)
    svg_path = models.CharField(max_length=1000)

    def __str__(self):
        return self.platform
    

class Blog(models.Model):

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    short_description = models.CharField(max_length=255, blank=True, null=True)
    post = CKEditor5Field('Text', config_name='extends', blank=True, null=True)
    featured_image = models.ImageField(upload_to='featured_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)
    grammar_check = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.category} - {self.title}"