from django.shortcuts import get_object_or_404
from rest_framework import pagination, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated

from ads.models import Ad, Comment
from ads.serializers import AdSerializer, AdDetailSerializer, CommentSerializer
from users.permissions import IsOwner, IsAdmin
from django_filters.rest_framework import DjangoFilterBackend
from .filters import AdFilter


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    pagination_class = AdPagination
    permission_classes = [AllowAny, ]
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = AdFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.action in ['retrieve', 'destroy', 'create', 'update', 'partial_update', 'me']:
            return AdDetailSerializer
        return AdSerializer

    @action(detail=False, methods=['GET'])
    def me(self, request):
        ads = Ad.objects.filter(author=request.user)
        page = self.paginate_queryset(ads)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def get_permissions(self):
        permission_classes = [AllowAny, ]
        if self.action in ['retrieve', 'create']:
            permission_classes = [IsAuthenticated, ]
        if self.action in ['destroy', 'update', 'partial_update']:
            permission_classes = [IsAuthenticated | IsOwner | IsAdmin]

        return [permission() for permission in permission_classes]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = AdPagination

    def get_queryset(self):
        return Comment.objects.filter(ad=self.kwargs['ad_pk'])

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, ad=get_object_or_404(Ad, pk=self.kwargs['ad_pk']))

    def get_permissions(self):
        permission_classes = []
        if self.action in ['list', 'retrieve', 'create']:
            permission_classes = [IsAuthenticated, ]
        if self.action in ['destroy', 'update', 'partial_update']:
            permission_classes = [IsAuthenticated | IsOwner | IsAdmin]

        return [permission() for permission in permission_classes]
