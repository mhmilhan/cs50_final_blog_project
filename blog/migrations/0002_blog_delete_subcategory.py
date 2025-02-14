# Generated by Django 5.1.4 on 2024-12-31 16:26

import django.db.models.deletion
import django_ckeditor_5.fields
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(allow_unicode=True, max_length=255, unique=True)),
                ('short_description', models.CharField(blank=True, max_length=255, null=True)),
                ('post', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='Text')),
                ('featured_image', models.ImageField(upload_to='featured_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('is_featured', models.BooleanField(default=False)),
                ('grammar_check', models.BooleanField(default=False)),
                ('is_approved', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category')),
            ],
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]
