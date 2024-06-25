from rest_framework import routers
from .viewsets import UserViewSet

app_name="erd"

router =routers.DefaultRouter()
router.register('erd',UserViewSet)