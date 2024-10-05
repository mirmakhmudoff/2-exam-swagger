from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AboutViewSet, ContactViewSet, NewsViewSet, TeamMemberViewSet,
    PublicationViewSet, ReviewViewSet, SearchViewSet, ServiceViewSet
)

router = DefaultRouter()
router.register(r'about', AboutViewSet, basename='about')
router.register(r'contact', ContactViewSet, basename='contact')
router.register(r'news', NewsViewSet, basename='news')
router.register(r'team-member', TeamMemberViewSet, basename='team-member')
router.register(r'publications', PublicationViewSet, basename='publications')
router.register(r'reviews', ReviewViewSet, basename='reviews')
router.register(r'search', SearchViewSet, basename='search')
router.register(r'services', ServiceViewSet, basename='services')

urlpatterns = [
    path('', include(router.urls)),
]
