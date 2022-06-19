from django.urls import path

from .views import PostList, PostDetail, UserRegister, UserData, GetUser
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("register/", UserRegister.as_view(), name="register"),
    path("users/data/", UserData.as_view(), name="users_data"),
    path("get/user/<int:pk>/", GetUser.as_view(), name="get_user"),
    path("posts/", PostList.as_view(), name="posts"),
    path("post/detail/<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("token/", TokenObtainPairView.as_view(), name="obtain_token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]