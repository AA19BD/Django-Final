import sys
import os
sys.path.append(os.getcwd())
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.db import models
from utils.constants import USER_ROLES, USER_SEX_MALE, USER_ROLE_GUEST, USER_SEX



class MainUserManager(BaseUserManager):
    use_in_migrations=True

    def _create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError('email must be set')
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)

    def create_user(self,email,password,**extra_fields):
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email,password,**extra_fields)

    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('role', 1)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be set')

        return self._create_user(email,password,**extra_fields)




class MainUser(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(_('email_address'),unique=True)
    first_name=models.CharField(_('first_name'),max_length=50,blank=True)
    last_name=models.CharField(_('last_name'),max_length=50,blank=True)
    date_joined=models.DateTimeField(_('date_joined'),auto_now_add=True)
    sex=models.SmallIntegerField(choices=USER_SEX,default=USER_SEX_MALE)
    age=models.IntegerField(default=0)
    is_active =models.BooleanField(_('active'),default=True)
    is_staff=models.BooleanField(_('is_staff'),default=False)
    role=models.SmallIntegerField(choices=USER_ROLES,default=USER_ROLE_GUEST)

    objects = MainUserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name=_('users')
        verbose_name_plural=_('users')
