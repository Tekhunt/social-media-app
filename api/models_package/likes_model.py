from .post_model import Posts
from django.db import models
from django.contrib.auth.models import User


class Likes(models.Model):
    """like  comment"""

    posts = models.ForeignKey(Posts, related_name="likes", on_delete=models.CASCADE)
    liked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("posts", "liked_by")
