from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Profile(models.Model):
    User = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)


def __str__(self):
    return str(self.user)


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingAuthor = models.SmallIntegerField(default=0)


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()


class Advert(models.Model):
    TANK = 'танк'
    HILL = 'хиллы'
    DD = 'ДД'
    DILLER = 'торговец'
    GILDMASTER = 'гилдмастер'
    QUEST = 'Квестгивер'
    SMITH = 'Кузнец'
    SKINNER = 'Кожевник'
    WITCH = 'Зельевар'
    WIZARD = 'Мастер заклинаний'

    CATEGORY_CHOICES = (
        (TANK, 'танк'),
        (HILL, 'хиллы'),
        (DD, 'ДД'),
        (DILLER, 'торговец'),
        (GILDMASTER, 'гилдмастер'),
        (QUEST, 'Квестгивер'),
        (SMITH, 'Кузнец'),
        (SKINNER, 'Кожевник'),
        (WITCH, 'Зельевар'),
        (WIZARD, 'Мастер заклинаний'),
    )

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    dateCreation = models.DateTimeField(auto_now_add=True)
    CategoryType = models.CharField(max_length=17, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=128)
    text = models.TextField()

    def __str__(self):
        return f'{self.title.title()}: {self.text[:20]}'

    def get_absolute_url(self):
        return reverse('advert_detail', args=[str(self.id)])


class Respond(models.Model):
    respondAdvert = models.ForeignKey(Advert, on_delete=models.CASCADE)
    respondAuthor = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = models.TextField(max_length=128)
    dateCreation = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def __str__(self):
        return f'{self.respondAuthor}: {self.text[:20]}'

    def get_absolute_url(self):
        return reverse('advert_detail', args=[str(self.id)])