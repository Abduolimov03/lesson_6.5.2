from django.urls import path
from .views import (
    CameraList,
    CameraDetail,
    CameraCreate,
    CameraUpdate,
    CameraDelete
)

urlpatterns = [
    path('camera/', CameraList.as_view(), name='camera'),
    path('camera/<int:pk>/', CameraDetail.as_view(), name='camera-detail'),
    path('camera/create/', CameraCreate.as_view(), name='create-camera'),
    path('camera/update/<int:pk>/', CameraUpdate.as_view(), name='update-camera'),
    path('camera/delete/<int:pk>/', CameraDelete.as_view(), name='delete-camera'),
]
