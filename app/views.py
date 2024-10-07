from django.shortcuts import render
from app.models import Post
# Create your views here.
def postList(request):
  posts = Post.objects.filter(published_at__isnull = False)
  return render(
    request,
    'postList.html',
    {'posts': posts}
  )