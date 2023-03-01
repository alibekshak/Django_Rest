from rest_framework.routers import DefaultRouter
from .views import CategoryModelViewSet, NewsImageModelViewsSet, NewsModelViewsSet

router = DefaultRouter()

router.register('category', CategoryModelViewSet)
router.register('news', NewsModelViewsSet)
router.register('news_image', NewsImageModelViewsSet)

urlpatterns = router.urls
