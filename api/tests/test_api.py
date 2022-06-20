from rest_framework.test import APIClient
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from api.models import Post
from django.urls import resolve
from api.views import PostDetail, PostList

# POST_URL = reverse('posts:PostList')

class TestPost(TestCase):

    def test_post_url_is_resolved(self):
        url = reverse('posts')
        self.assertEquals(resolve(url).func.view_class, PostList)

    def test_post_detail_url_is_resolved(self):
        url = reverse('post_detail', args=[1])
        self.assertEquals(resolve(url).func.view_class, PostDetail)

