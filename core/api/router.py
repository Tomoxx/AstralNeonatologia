from rest_framework.routers import DefaultRouter
from core.api.views import RecienNacidoApiViewSet

router_posts = DefaultRouter()

router_posts.register(prefix='post', basename='post', viewset=RecienNacidoApiViewSet)

