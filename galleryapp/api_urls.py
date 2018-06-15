from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'galleries', views.GalleryViewSet)


urlpatterns = router.urls
