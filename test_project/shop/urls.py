from .views import ShopViewSet
from rest_framework.routers import DefaultRouter

handler500 = 'rest_framework.exceptions.server_error'

router = DefaultRouter()
router.register(r'', ShopViewSet, basename='shop')
urlpatterns = router.urls
'''from django.urls import path


from test_project.shop import views

urlpatterns = [
    path('', views.ShopViewSet.as_view({'get': 'list', 'post': 'create'})),
]
'''

