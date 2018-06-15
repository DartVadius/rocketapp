from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'posts', views.PostsViewSet)


urlpatterns = router.urls
