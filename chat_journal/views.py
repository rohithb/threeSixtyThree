import json
from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render_to_response
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import RequestContext
from .forms import EntryForm
from .models import Post

class LoggedInMixin(object):

    '''
        A mixin that can be used with classes that require a logged in user to use it.
        Use LoggedInMixin as first superclass with each class.
    '''
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)

class HomePage(LoggedInMixin, View):
    def get(self, request):
        form = EntryForm()
        return render_to_response('chat_journal/home_page.html', {'form': form}, context_instance=RequestContext(request))


class SavePost(LoggedInMixin, View):
    def post(self, request):
        form = EntryForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return HttpResponse(json.dumps(form.instance.as_json()), content_type='json')
        else:
            return HttpResponse('False', status=450)


class ListPosts(LoggedInMixin, View):
    def get(self, request):
        user = request.user
        posts = Post.objects.filter(user=user)
        posts_json = [post.as_json() for post in posts]
        return HttpResponse(json.dumps(posts_json), content_type='json')


class DeletePost(LoggedInMixin, View):
    def post(self, request, *args, **kwargs):
        pk = kwargs['pk']
        Post.objects.get(pk=pk, user=request.user).delete()
        return HttpResponse('Success')


class GetSinglePost(LoggedInMixin, View):
    def get(self, request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs['pk'], user=request.user)
        return HttpResponse(json.dumps(post.as_json()), content_type='json')