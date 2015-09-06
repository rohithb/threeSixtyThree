from django.contrib.auth.models import User
from django.views.generic import TemplateView
from rest_framework import permissions, viewsets
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from journal.models import Post
from journal.permissions import IsAuthenticated
from journal.serializers import PostSerializer, UserSerializer


class LoggedInMixin(object):
    '''
        To ensure the user is logged authenticated
        Use this class as the first superclass.
    '''
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)


class Index(LoggedInMixin, TemplateView):
    template_name = 'journal/index.html'


class PostViewSet(LoggedInMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_Classes = (permissions.IsAuthenticated, IsAuthenticated)

    def get_queryset(self):
        queryset = super(PostViewSet, self).get_queryset()
        # queryset = queryset.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserViewSet(LoggedInMixin, viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
