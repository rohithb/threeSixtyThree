from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from rest_framework import permissions, viewsets

from journal.models import Post
from journal.permissions import IsAuthenticated
from journal.serializers import PostSerializer, UserSerializer


@csrf_protect
@ensure_csrf_cookie
def index(request):
    user = authenticate(username='rohith', password='microsoft')
    if user is not None:
        login(request, user)
        return render(request, 'journal/index.html')


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_Classes = (permissions.IsAuthenticated, IsAuthenticated)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
