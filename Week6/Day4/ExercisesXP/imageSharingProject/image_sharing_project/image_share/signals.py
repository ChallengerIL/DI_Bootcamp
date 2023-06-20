from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile, Image


#  def profile_creation_signal(sender, instance, created, **kwargs) :
#
#     if created:
#         UserProfile.objects.create(pk=instance.id, user=instance)
#
# post_save.connect(profile_creation_signal, sender=User)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(pk=instance.id, user=instance)


post_save.connect(create_user_profile, sender=User)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


post_save.connect(save_user_profile, sender=User)


@receiver(post_save, sender=Image)
def increase_image_count(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile.objects.get(user=instance.user)
        user_profile.uploads_count += 1
        user_profile.save()


post_save.connect(increase_image_count, sender=Image)
