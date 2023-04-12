from django.db import models
from imagekit.processors import Thumbnail
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
    # thumbnail_img = ProcessedImageField(
    #     blank = True,
    #     upload_to = 'thumbnail/',
    #     processors = [ResizeToFill(200,300)], # 200*300으로 줄이자.
    #     format='JPEG',
    #     options={'quality':80},  # django-imagekit 에 가면 설정들 나와 있음
    # )
    thmbnail_img = ImageSpecField(
        source='image',
        processors=[Thumbnail(200,300)], # 200*300으로 줄이자
        format = 'JPEG',
        options = {'quality':80},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}번째글 - {self.title}'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)  # 댓글이 무제한이면 구성이 엉망이 될 수 있음