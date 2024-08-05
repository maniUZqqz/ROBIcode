from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser




class User(AbstractUser):
    mobile = models.CharField(max_length=12, null=True, blank=True, verbose_name='تلفن')
    email_active = models.EmailField(null=False, blank=True, verbose_name='Email', unique=True, editable=False)
    image = models.ImageField(upload_to='upload/profile/', null=True, blank=True)


    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"

    def __str__(self):
        return self.get_full_name()
