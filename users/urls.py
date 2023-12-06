# from django.urls import path
from rest_framework import routers
from users.views import (UserAPI, UserSettingsAPI)

router = routers.DefaultRouter()

router.register('users', UserAPI)
router.register('user/settings', UserSettingsAPI)

urlpatterns = [
]

urlpatterns += router.urls
