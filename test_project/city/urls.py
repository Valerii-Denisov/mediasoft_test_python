from django.urls import path


from test_project.city import views

urlpatterns = [
    path('', views.CityViewSet.as_view({'get': 'list'}),),
    path('<int:pk>/street/', views.StreetViewSet.as_view({'get': 'list'}), name='city-detail'),
]
