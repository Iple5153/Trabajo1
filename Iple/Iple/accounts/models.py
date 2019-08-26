from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.DO_NOTHING,)
	Descripcion = models.CharField(max_length=100, default='')
	Ciudad = models.CharField(max_length=100, default='')
	Sitio_Web = models.URLField(default='')
	Telefono = models.IntegerField(default=0)

def create_profile(sender, **kwargs):

        if kwargs['created']:
        	user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)