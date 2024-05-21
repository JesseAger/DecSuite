# core/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RequestLogViewSet, ThreatViewSet

router = DefaultRouter()
router.register(r'request-logs', RequestLogViewSet)
router.register(r'threats', ThreatViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('requestlogView/', RequestLogViewSet.as_view, name='request' ),
    path('threatview/', ThreatViewSet.as_view, name='threat'),
]

