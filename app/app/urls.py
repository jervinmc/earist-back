from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.urls.conf import include
from room.views import RoomBuilding
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('api/v1/users/', include('users.urls')),
    path('api/v1/building/', include('building.urls')),
    path('api/v1/room/', include('room.urls')),
     path('api/v1/floor/', include('floor.urls')),
    path('api/v1/room-building', RoomBuilding.as_view(), name='get_user'),



]