from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from .models import User

@receiver(user_logged_in)
def set_online(sender, request, user, **kwargs):
    if isinstance(user, User):
        user.is_online = True
        user.save()

@receiver(user_logged_out)
def set_offline(sender, request, user, **kwargs):
    if isinstance(user, User):
        user.is_online = False
        user.save()
