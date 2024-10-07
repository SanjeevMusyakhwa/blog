from django.shortcuts import render, redirect
from app.models import Post
# Create your views here.
def postList(request):
  posts = Post.objects.filter(published_at__isnull = False)
  return render(
    request,
    'postList.html',
    {'posts': posts}
  )

def postDetail(request, pk):
  post = Post.objects.get(id = pk)
  return render(
    request,
    'postDetail.html',
    {'post': post}
  )


def postDelete(request, pk):
  post = Post.objects.get(id = pk)
  post.delete()
  return redirect('postList')

def postUpdate(request, pk):
  post = Post.objects.get(id = pk)
  if request.method == 'POST':
    post.title = request.POST['title']
    post.content = request.POST['content']
    post.save()
    return redirect('postList')
  return render(
    request,
    'postUpdate.html',
    {'post':post}
  )
