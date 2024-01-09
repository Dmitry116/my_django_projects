from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #on_delete если пользователь удален, удаляется его профиль
    bio = models.TextField(max_length=500, blank=True)  #blank=True позволяет сохранять пустые значения
    agreement_accepted = models.BooleanField(default=False) #пользовательское соглашение
