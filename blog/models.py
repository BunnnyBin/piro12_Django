from django.db import models
from askcompany.utils import uuid_upload_to

class Post(models.Model):
    author_name = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField(blank=True, upload_to=uuid_upload_to)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # Comment가 Post를 상속받는데 Post가 삭제되면 따라서 삭제되는 걸로
    message = models.TextField()