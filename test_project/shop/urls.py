from django.urls import path


from test_project.shop import views

urlpatterns = [
    path('', views.ShopViewSet.as_view({'get': 'list'})),
]
