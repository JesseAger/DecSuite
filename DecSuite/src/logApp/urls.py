# logApp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DetailedLogViewSet

router = DefaultRouter()
router.register(r'detailed-logs', DetailedLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
