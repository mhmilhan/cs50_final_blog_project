from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog
from .forms import PostForm
from django.core.paginator import Paginator
from django.template.defaultfilters import slugify

# Create your views here.
def add_post_view(request, category):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            title = form.cleaned_data['title']
            # Generate Unicode-friendly slug
            post.slug = slugify(title)
            post.save()
            return redirect('success_view')
    else:
        form = PostForm()
    context = {
        'form': form,
        'category': category,
    }
    return render(request, 'blog/add_post.html', context)

def success_view(request):
    return render(request, 'blog/success_page.html')

def post_by_category(request, category):
    featured_post_list = Blog.objects.filter(
        category__category_name=category,  # Use __name to filter by Category's name field
        is_featured=True
    ).order_by('-published_at')[:4]

    post_list = Blog.objects.filter(
        category__category_name=category,  # Use __name to filter by Category's name field
        is_approved=True
    ).order_by('-published_at')

        # Pagination for post_list
    paginator = Paginator(post_list, 2)  # Show 8 posts per page (you can adjust this as needed)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'featured_post_list': featured_post_list,
        'post_list': page_obj,
    }
    return render(request, 'blog/post_by_category.html', context)


def post_detail(request, category, post_id):
    full_post = get_object_or_404(Blog, uuid=post_id, category__category_name=category, is_approved=True)
    context = {
        'full_post': full_post,
    }
    return render(request, 'blog/post_detail.html', context)