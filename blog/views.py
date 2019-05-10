from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from .models import Post

def post_list(request):
    name="Vani"
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts, 'name': name})
#ruft funktion post list auf aus ordner views
#render= dargestellt werden