from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    # модель истории игрока
    # тут потенциальная ошибка USER
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.CharField(max_length=50)
    data_scope = models.DateTimeField(auto_now_add=True)
    top_score = models.CharField(max_length=50)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

