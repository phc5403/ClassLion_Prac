from django.shortcuts import render
from django.utils import timezone

from django.urls import reverse_lazy
from django.views.generic.list import ListView # 데이터 뿌리기
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView # 데이터 추가
from .models import ClassBlog

# Create your views here.

# CBV는 html에 대한 규약이 존재함. 
# -> Default로 지정된 html이름을 준수해야함. 마음대로 짓고싶으면 따로 명시해야함.

# 글 목록 보여주기
class BlogView(ListView): # Blog 리스트를 담은 html이 필요함 : (소문자모델)_list.html
    # ClassBlog 모델로부터 만들어진 객체의 목록
    model = ClassBlog

'''
# html 이름을 커스터마이징 할때.
class BlogView(ListView):
    # html 이름을 커스터마이징 할 때.
    template_name = 'classcrud/list.html'
    
    # 객체를 Object로 표현한다면 서로 다른 객체는 어떻게 구분하나?
    # 객체 이름을 커스터마이징 할 때.
    context_object_name = 'blog_list'
    model = ClassBlog
'''

class BlogCreate(CreateView): # form(입력공간)을 담은 html이 필요함 : (소문자모델)_form.html
    model = ClassBlog
    fields = ['title', 'body']
    
    # 블로그 객체가 성공적으로 만들어지면, redirect하는 것
    success_url = reverse_lazy('list')

class BlogDetail(DetailView): # 상세 내용을 담은 html이 필요함 : (소문자모델)_detail.html
    model = ClassBlog

class BlogUpdate(UpdateView): # form(입력공간)을 담은 html이 필요함 : (소문자모델)_form.html
    model = ClassBlog
    fields = ['title', 'body']
    success_url = reverse_lazy('list')
    
class BlogDelete(DeleteView): # 진짜 지울지 확인메시지를 담은 html이 필요함 : (소문자모델)_confirm_delete.html
    model = ClassBlog
    success_url = reverse_lazy('list')