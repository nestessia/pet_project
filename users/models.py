from django.contrib.auth.models import AbstractUser
from django.db import models

USER = 'Пользователь'
ADMIN = 'admin'
MASTER = 'Мастер'

ROLE_CHOICES = [
    (USER, USER),
    (MASTER, MASTER),
]


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=50,
                                  blank=True)
    last_name = models.CharField(max_length=50,
                                 blank=True)
    role = models.CharField(max_length=150,
                            blank=True,
                            choices=ROLE_CHOICES,
                            default=USER,)
    telephone = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    confirmation_code = models.CharField('Код подтверждения',
                                         max_length=100,
                                         null=True)

    @property
    def is_user(self):
        return self.role == USER

    @property
    def is_admin(self):
        return self.role == ADMIN

    @property
    def is_master(self):
        return self.role == MASTER

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("id",)


