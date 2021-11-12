# from .views import RegisterAPI
from django.urls import path

from .views import RegisterAPI, LoginAPI
from .views import user_list, UserInfo


urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/user_list/', user_list),
    path('api/UserInfo/<int:pk>/', UserInfo)
]
