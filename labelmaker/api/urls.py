from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from . import views

router = routers.DefaultRouter()
router.register('labels', views.LabelView)

urlpatterns = [
    path('', include(router.urls)),
    path('users/', views.UserList.as_view()),
    path('users/create/', views.UserCreate.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('login', obtain_auth_token),
]