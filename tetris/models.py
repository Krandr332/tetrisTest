from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

"Модель для записи результатов игр"


class Profile(models.Model):
    # модель истории игрока
    # тут потенциальная ошибка USER
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.CharField(max_length=50, default=0)
    data_scope = models.DateTimeField(auto_now_add=True)
    top_score = models.CharField(max_length=50, default=0)

    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)

    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()

    @receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
    def save_profile(sender, instance, created, **kwargs):
        user = instance
        if created:
            profile = Profile(user=user)
            profile.save()

    def __str__(self):
        return f'{self.user.username}'


class Message(models.Model):
    username = models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)
