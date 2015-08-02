from rest_framework import serializers
from django.contrib.auth.models import User

from journal.models import Post


class UserSerializer(serializers.ModelSerializer):
    # posts = PostSerializer(many=True, source='post_set')

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'last_login')


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('body', 'user', 'timestamp')

    def validate_body(self, value):
        if len(value) < 1:
            raise serializers.ValidationError("Post is too short")
        return value
