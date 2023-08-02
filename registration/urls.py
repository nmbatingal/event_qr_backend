from django.urls import path
from rest_framework.routers import DefaultRouter
# from .views import RegistrationViewSet, get_events
from .views import register_user, get_events

router = DefaultRouter()
# router.register(r'register', RegistrationViewSet, basename='register')
urlpatterns = router.urls

urlpatterns += [
    # path('register/<uuid:document_id>/qr_code/', get_qr_code, name='get_qr_code'),
    path('register/', register_user, name='register_user'),
    path('events/', get_events, name='get_events'),
]