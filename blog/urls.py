from django.urls import path,include
from .views import Myblog,myblog2,myblog3,myblog4,myblog5,newblog
urlpatterns = [
    path('',Myblog.as_view(), name='home'),
    path('myblog2/',myblog2,name='about'),
    path('myblog3/',myblog3,name='myblog3'),
    path('myblog4/',myblog4,name='contact'),
    path('myblog5/<int:pk>',myblog5, name='blog'),
    path('new/',newblog.as_view(), name='post'),
]

