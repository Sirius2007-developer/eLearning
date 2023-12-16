from django.db import models
from django.utils import timezone

# Create your models here.
class Gallery(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='base/img')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='index/img')
    number = models.TextField()

    def __str__(self):
        return self.name


class Course(models.Model):
    img = models.ImageField(upload_to='index/img')
    name = models.TextField()
    cost = models.IntegerField()
    tutor = models.CharField(max_length=200)
    time = models.FloatField()
    count = models.IntegerField()
    numb = models.IntegerField()

    def __str__(self):
        return self.tutor

class Team(models.Model):
    img = models.ImageField(upload_to='index/img')
    name = models.TextField()
    rank = models.TextField()

    def __str__(self):
        return self.name

class Test(models.Model):
    img = models.ImageField(upload_to='index/img')
    name = models.TextField()
    job = models.TextField()
    bio = models.TextField()

    def __str__(self):
        return self.name

class Carousel(models.Model):
    img = models.ImageField(upload_to='index/img')
    name = models.CharField(max_length=200)
    bio = models.TextField()
    title = models.TextField()

    def __str__(self):
        return self.name

class Newsletter(models.Model):
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.email


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name



# <--------Filterlar------->
# class News(models.Model):
#
#     class Status(models.TextChoices):
#         Draft = "DF", "Draft"
#         Published = "PB", "Published"
#     title = models.CharField(max_length=200)
#     slug = models.SlugField(max_length=200)
#     body = models.TextField()
#     image = models.ImageField(upload_to='news/images')
#     category = models.ForeignKey()
#     published_time = models.DateTimeField(default=timezone.now)
#     created_time = models.DateTimeField(auto_now_add=True)
#     updated_time = models.DateTimeField(auto_now=True)
#     status = models.CharField(max_length=2)

    # --Draft - qoralama
    # --Published = tayyor














