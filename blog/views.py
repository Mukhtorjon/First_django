from django.shortcuts import render
from .models import Blog
from django.http import HttpResponse
from datetime import datetime
from django.template import loader
from django.views.generic.edit import CreateView
from django.views.generic import ListView,DetailView

# Create your views here.
# def myblog(requests):
#     blogs=Blog.objects.all()
#     context={"blogs":blogs}
#     return render(requests,'index.html',context=context)
class Myblog(ListView):
    model=Blog
    template_name="index.html"


def myblog2(requests):
    return render(request=requests,template_name="about.html")
def myblog3(requests):
    return render(request=requests,template_name="Shablon.html")
def myblog4(requests):
    return render(request=requests,template_name="contact.html")
# class Myblog5(DetailView):
#     model=Blog
#     template_name='blog.html'
#     context_object_name='blog'
#     blogs=Blog.objects.all()
   
    
def myblog5(requests,pk):
    blog=Blog.objects.get(pk=pk)
    blogs=Blog.objects.all()[:3]
    context={"blog":blog,"blogs":blogs}
    return render(requests,"blog.html",context=context)


class newblog(CreateView):
    model=Blog
    template_name="post.html"
    fields=['aftor','title','photo','text']