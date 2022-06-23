from django.urls import path

from .views import PostList, PostDetail, UserRegister, UserData, GetUser, UpdatePost, LikeList, LikeDetail, DisLikeList, DisLikeDetail
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("register/", UserRegister.as_view(), name="register"),
    path("users/data/", UserData.as_view(), name="users_data"),
    path("get/user/<int:pk>/", GetUser.as_view(), name="get_user"),
    path("posts/", PostList.as_view(), name="posts"),
    path("post/detail/<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("update/<int:pk>/", UpdatePost.as_view(), name="update_detail"),
    path("likes/", LikeList.as_view(), name="likes"),
    path("likes/detail/<int:pk>/", LikeDetail.as_view(), name="like_detail"),
    path("dislikes/", DisLikeList.as_view(), name="dislikes"),
    path("dislikes/detail/<int:pk>/", DisLikeDetail.as_view(), name="dislike_detail"),
    path("token/", TokenObtainPairView.as_view(), name="obtain_token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]