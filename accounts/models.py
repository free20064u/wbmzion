from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField 
from pilkit.processors import ResizeToFill
from django.utils.translation import gettext_lazy as _

from .manager import CustomUserManager


# Create your models here.
class CustomUser(AbstractUser):
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    image = ProcessedImageField(blank=True, null=True,default='profile/wbm-logo.png', upload_to='profile',processors=[ResizeToFill(100, 100)],format='JPEG',options={'quality': 60})
    is_active = models.BooleanField(default=True)
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=200, default='', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()