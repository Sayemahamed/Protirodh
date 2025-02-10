from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base.html')

def index(request, *args, **kwargs):
    return render(request, 'dummy_feed.html', {})

def detail(request, post_id):
    return render(request, 'dummy_post_detail.html', {'post_id': post_id})

def search(request):
    return render(request, 'dummy_search.html')