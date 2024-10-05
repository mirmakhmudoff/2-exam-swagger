from django.core.mail import send_mail
from rest_framework import mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination

from .models import About, News, TeamMember, Publication, Review, Search, Service, Contact
from .serializers import (
    AboutSerializer, NewsSerializer, TeamMemberSerializer, PublicationSerializer,
    ReviewSerializer, SearchSerializer, ServiceSerializer, ContactSerializer
)


class ContactViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        contact = serializer.save()

        send_mail(
            subject=f"New Contact Request from {contact.name}",
            message=f"Name: {contact.name}\nEmail: {contact.email}\nMessage: {contact.message}",
            from_email='your_email@example.com',
            recipient_list=['admin@example.com'],
            fail_silently=False,
        )


class AboutViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class NewsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class TeamMemberViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer


class PublicationViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer


class ReviewViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class SearchPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100


class SearchViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Search.objects.all()
    serializer_class = SearchSerializer
    pagination_class = SearchPagination


class ServiceViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
