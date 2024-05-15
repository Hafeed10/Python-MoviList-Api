from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import Group, Permission
from django.utils.translation import gettext_lazy as _

class Movie(models.Model):
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    director = models.CharField(max_length=100)
    protagonist = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    releasing_date = models.DateField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='custom_user_permissions',
        help_text=_('Specific permissions for this user.'),
    )

    class Meta:
        app_label = 'movies'



class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.PositiveIntegerField()
    director = models.CharField(max_length=100)

    def __str__(self):
        return self.title