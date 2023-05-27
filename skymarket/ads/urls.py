from django.urls import include, path
from rest_framework import routers

from ads.views import AdViewSet, CommentViewSet

ad_router = routers.SimpleRouter()
ad_router.register('ads', AdViewSet)

comment_router = routers.SimpleRouter()
comment_router.register('comments', CommentViewSet)

urlpatterns = [
    path('ads/<int:ad_pk>/', include(comment_router.urls)),
    path('ads/<int:ad_pk>/comments/<int:comment_id>/', include(comment_router.urls))
]

urlpatterns += ad_router.urls + comment_router.urls
