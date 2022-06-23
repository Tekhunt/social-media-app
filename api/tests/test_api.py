from rest_framework.test import APIClient
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from api.models import Post
from django.urls import resolve
from api.views import GetUser, LikeList, PostDetail, PostList, UpdatePost, UserData, UserRegister, LikeDetail, DisLikeList, DisLikeDetail


class TestPost(TestCase):
    def test_post_url_is_resolved(self):
        url = reverse("posts")
        self.assertEquals(resolve(url).func.view_class, PostList)

    def test_post_detail_url_is_resolved(self):
        url = reverse("post_detail", args=[1])
        self.assertEquals(resolve(url).func.view_class, PostDetail)

    def test_register_url_is_resolved(self):
        url = reverse("register")
        self.assertEquals(resolve(url).func.view_class, UserRegister)

    def test_userdata_detail_url_is_resolved(self):
        url = reverse("users_data")
        self.assertEquals(resolve(url).func.view_class, UserData)

    def test_getuser_detail_url_is_resolved(self):
        url = reverse("get_user", args=[1])
        self.assertEquals(resolve(url).func.view_class, GetUser)

    def test_update_detail_url_is_resolved(self):
        url = reverse("update_detail", args=[1])
        self.assertEquals(resolve(url).func.view_class, UpdatePost)


    def test_likes_url_is_resolved(self):
        url = reverse("likes")
        self.assertEquals(resolve(url).func.view_class, LikeList)

    def test_like_detail_url_is_resolved(self):
        url = reverse("like_detail", args=[1])
        self.assertEquals(resolve(url).func.view_class, LikeDetail)

    def test_dislikes_url_is_resolved(self):
        url = reverse("dislikes")
        self.assertEquals(resolve(url).func.view_class, DisLikeList)

    def test_dislike_detail_url_is_resolved(self):
        url = reverse("dislike_detail", args=[1])
        self.assertEquals(resolve(url).func.view_class, DisLikeDetail)
