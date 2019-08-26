from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog
from .forms import NewBlog

# Create your views here.

def welcome(request):
    return render(request, 'funccrud/index.html')
    
def read(request):
    blogs = Blog.objects.all()
    return render(request, 'funccrud/funccrud.html', {'blogs' : blogs})
    
def create(request):
    if request.method == 'POST':
        form = NewBlog(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    
    else:
        form = NewBlog()
        return render(request, 'funccrud/new.html', {'form' : form})
    
def update(request, pk):
    # 1. 어떤 글을 수정할지 해당 블로그 객체를 갖고오기
    blog = get_object_or_404(Blog, pk=pk)
    
    # 2. 해당하는 블로그 객체번호의 입력공간을 갖고오기
    form = NewBlog(request.POST, instance=blog) # instance=객체
    
    if form.is_valid():
        form.save()
        return redirect('home')
        
    return render(request, 'funccrud/new.html', {'form' : form})
    
def delete(reqeust, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect('home')
