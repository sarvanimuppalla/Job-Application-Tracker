from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import JobHandler



router = DefaultRouter()
router.register('jobs', JobHandler, basename='jobs')


urlpatterns = router.urls
