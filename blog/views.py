from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def blog(request):
    blog = Blog.objects
    return render(request, 'blog/blog.html', {'blog':blog})

def content(request, blog_id):
    content = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/content.html', {'blog':content})