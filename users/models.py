from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = models.CharField(max_length=150, **NULLABLE)
    surname = models.CharField(max_length=50)
    email = models.EmailField(unique=True, verbose_name='почта')
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    side = models.CharField(max_length=100, verbose_name='страна', **NULLABLE)

    class Meta:
        permissions = [
            (
                'manager_site',
                'Менеджер'
            )
        ]
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ('id',)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


