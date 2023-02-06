from .views import ShopViewSet
from rest_framework.routers import DefaultRouter

handler500 = 'rest_framework.exceptions.server_error'

router = DefaultRouter()
router.register(r'', ShopViewSet, basename='shop')
urlpatterns = router.urls
