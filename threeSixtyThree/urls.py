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
from django.conf.urls import include, url

urlpatterns = [
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name="login"),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/accounts/login/'}),
    url(r'^accounts/password-change/$', 'django.contrib.auth.views.password_change',
        {'post_change_redirect': '/'}),
    url(r'', include('journal.urls', namespace='home')),
]
