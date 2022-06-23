from .post_model import Posts
from django.db import models
from django.contrib.auth.models import User


class DisLikes(models.Model):
    """Dislike  comment"""

    posts = models.ForeignKey(Posts, related_name="dis_likes", on_delete=models.CASCADE)
    dis_liked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
