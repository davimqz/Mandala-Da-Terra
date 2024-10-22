# contas/models.py

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, cpf, password=None, **extra_fields):
        if not cpf:
            raise ValueError('O CPF deve ser definido')
        user = self.model(cpf=cpf, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, cpf, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(cpf, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    cpf = models.CharField(max_length=11, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'cpf'  # Define o CPF como o campo de identificação
    REQUIRED_FIELDS = []  # Outros campos obrigatórios, se houver

    def __str__(self):
        return self.cpf  # Representação do usuárioaaa




