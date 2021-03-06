from rest_framework import serializers
from django.contrib.auth.models import User

from journal.models import Post, Profile


class UserProfileSerializer(serializers.ModelSerializer):
    # posts = PostSerializer(many=True, source='post_set')

    class Meta:
        model = Profile
        fields = ('display_picture',)


class UserSerializer(serializers.ModelSerializer):
    # posts = PostSerializer(many=True, source='post_set')
    profile = UserProfileSerializer()
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'last_login', 'profile')


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'body', 'user', 'timestamp')

    def validate_body(self, value):
        if len(value) < 1:
            raise serializers.ValidationError("Post is too short")
        return value
