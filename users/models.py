from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
from django.utils.timezone import now
from datetime import timedelta


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True)
    age = models.PositiveIntegerField(default=18)
    email = models.EmailField(_('email address'), blank=True, unique=True)

    activation_key = models.CharField(max_length=128, blank=True, null=True)
    activation_key_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def is_activation_key_expired(self):
        if now() <= self.activation_key_created + timedelta(hours=48):
            return False
        else:
            return True