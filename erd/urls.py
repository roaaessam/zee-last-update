from django.urls import path,include
from .import views 
from rest_framework.routers import DefaultRouter
from erd import router as users_api_router
from .viewsets import RegisterViewSet 

router = DefaultRouter()
router.register(r'register', RegisterViewSet)


api_url_patterns=[
    path(r'accounts/',include(users_api_router.router.urls))
]


router = DefaultRouter()
router.register(r'patient', views.GetPatient,basename='patient')
router.register(r'Profile', views.UserSerializer,basename='Profile')
router.register(r'Escort', views.GetEscort,basename='Escort')
router.register(r'Reminder', views.GetReminder,basename='Reminder')
router.register(r'Diseases', views.GetDiseases,basename='Diseases')
router.register(r'Document', views.GetDocument,basename='Document')
router.register(r'Medicine', views.GetMedicine,basename='Medicine')
router.register(r'Register', views.GetRegister,basename='Register')
# router.register(r'Login', views.GetLogin,basename='Login')


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/',include(api_url_patterns)),
]
# urlpatterns += router.urls
