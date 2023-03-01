from rest_framework import serializers
from .models import Category, News, NewsImages


class NewsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImages
        fields = ('id', 'news', 'image')


class GetNewsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImages
        fields = ('image')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", 'title', 'slug')


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'category', 'image', 'text', 'created_at')


class GetNewsSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(read_only=True, slug_field=True)
    news_image = GetNewsImageSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = ('id', 'title', 'category', 'image', 'text', 'created_at', 'news_image')
