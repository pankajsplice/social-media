from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField


class Contact(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, help_text="Name")
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(max_length=1000, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name


class Newsletter(models.Model):

    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.email


class Blog(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    icon = models.ImageField(upload_to="images/", null=True, blank=True)
    content = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    published_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
