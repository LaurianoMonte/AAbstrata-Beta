from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    short_description = RichTextField()
    content = RichTextUploadingField()
    date = models.DateField(default=timezone.now)
    author = models.CharField(max_length=200)
    post_image = models.ImageField(blank=True, upload_to='photos/%Y/%m')

    def publish(self):
        self.date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
