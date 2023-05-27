from rest_framework import serializers

from users.models import User
from .models import Ad, Comment


class CommentSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    author_image = serializers.ImageField(source='author.image', read_only=True)
    ad = serializers.PrimaryKeyRelatedField(read_only=True, required=False)
    author = serializers.PrimaryKeyRelatedField(required=False, read_only=True)

    class Meta:
        model = Comment
        fields = ['pk', 'text', 'author', 'created_at', 'author_first_name', 'author_last_name', 'ad', 'author_image']


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['pk', 'image', 'title', 'price', 'description']


class AdDetailSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(source='author.phone', read_only=True)
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    author = serializers.PrimaryKeyRelatedField(required=False, read_only=True)

    class Meta:
        model = Ad
        fields = ['pk', 'image', 'title', 'price', 'phone', 'description', 'author_first_name', 'author_last_name',
                  'author']
