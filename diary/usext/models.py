from django.db import models
from django.contrib.auth.models import User

class UserExtends(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.ImageField(null=True, blank=True, verbose_name='Аватарка')
	vip = models.DateTimeField(help_text='Дата по которую пользователь имеет ВИП-статус')
