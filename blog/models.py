from django.db import models


# Create your models here.
class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(TimeStampedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(TimeStampedModel):
    image = models.ImageField(upload_to='posts/')
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Author(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='authors/')

    def __str__(self):
        return self.name


class Gallery(TimeStampedModel):
    image = models.ImageField(upload_to='gallery/')
    title = models.CharField(max_length=255)


class About(TimeStampedModel):
    image = models.ImageField(upload_to='about/')
    name = models.CharField(max_length=255)
    description = models.TextField()
    # author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Pricing(TimeStampedModel):
    title = models.CharField(max_length=255)
    photos = models.CharField(max_length=255)
    processing = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    resolution = models.CharField(max_length=255)
    term = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='pricing/')


class Contact(TimeStampedModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name


class In_Touch(TimeStampedModel):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.CharField(max_length=255)

    def __str__(self):
        return self.address
