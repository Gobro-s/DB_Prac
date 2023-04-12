from django.db import models
from django.conf import settings


# Create your models here.
class Hashtag(models.Model):
    content = models.CharField(
        unique=True, max_length=20
    )  # 이미 존재하는 hashtag면 굳이 새로 만들 필요 X


class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_articles"
    )
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hashtags = models.ManyToManyField(Hashtag)

    def __str__(self):
        return f"{self.id}번째글 - {self.title}"


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # parent : 답글(대댓글)필드
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, related_name="replies"
    )

    def __str__(self):
        return self.content
