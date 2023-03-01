from rest_framework.viewsets import ModelViewSet
from .models import Category, News, NewsImages
from .serializers import CategorySerializer, NewsSerializer, NewsImageSerializer,GetNewsSerializer, NewsImages


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class NewsModelViewsSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get_serializer_class(self):
        if self.request.method in ("GET", "HEAD", "OPTIONS"):
            return GetNewsSerializer

        return NewsSerializer


class NewsImageModelViewsSet(ModelViewSet):
    queryset = NewsImages.objects.all()
    serializer_class = NewsImageSerializer

