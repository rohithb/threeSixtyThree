"""threeSixtyThree URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from chat_journal import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='homepage'),
    url(r'^save-post/$', views.SavePost.as_view(), name='save-post'),
    url(r'^delete-post/(?P<pk>\d+)/$', views.DeletePost.as_view(), name='delete-post'),
    url(r'^list-posts/$', views.ListPosts.as_view(), name='list-posts'),
    url(r'^post/(?P<pk>\d+)/$', views.GetSinglePost.as_view(), name='get-single-post'),
]

