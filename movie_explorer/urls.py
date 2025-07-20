from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from movies.views import MovieViewSet, ActorViewSet, DirectorViewSet, GenreViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Movie Explorer API",
        default_version='v1',
        description="Explore Movies, Actors, Directors, and Genres",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register('movies', MovieViewSet)
router.register('actors', ActorViewSet)
router.register('directors', DirectorViewSet)
router.register('genres', GenreViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # Use ReDoc (works without installing swagger-ui templates)
    path('swagger/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
