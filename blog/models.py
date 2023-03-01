from django.db import models
from autoslug import AutoSlugField


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = AutoSlugField(populate_from='title', unique=True)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='news/')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class NewsImages(models.Model):
    news: News = models.ForeignKey(News, on_delete=models.CASCADE, related_name='news_image')
    image = models.ImageField(upload_to='news/')

    def __str__(self):
        return self.news.title
