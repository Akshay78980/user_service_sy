from django.urls import path, include
from users.views import CustomUserViewSet, UserProfileViewSet, UserRegistrationAPI
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users',CustomUserViewSet, basename='user')
router.register(r'profiles',UserProfileViewSet,basename='profile')

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('', include(router.urls)),
    path('user/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user-token-refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('user/registration/',UserRegistrationAPI.as_view(), name='user_registration')
]

