from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from . import views


app_name = 'accountapp'

router = DefaultRouter()
router.register(prefix=r'create', basename='account-registration', viewset=views.AccountRegistrationGenericViewSet)

urlpatterns = [
    path(route='registration/', view=include(router.urls)),
    path(route='signin/', view=TokenObtainPairView.as_view(), name='auth-signin'),
    path(route='token/refresh/', view=TokenRefreshView.as_view(), name='token-refresh'),
    path(route='token/verify/', view=TokenVerifyView.as_view(), name='token-verify'),
    path(route='signout/', view=views.SignoutView.as_view(), name='auth-signout'),
]