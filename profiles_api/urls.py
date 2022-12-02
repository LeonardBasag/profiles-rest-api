from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet) # we dont need to specify a basename because of queryset in the viewset

urlpatterns = [
    path('hello-view', views.HelloApiView.as_view()),
    path('', include(router.urls))
]