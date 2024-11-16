from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Profile, Role
from django.contrib.auth.models import User


@receiver(post_save, sender=Profile)
def assign_default_role_to_client(sender, instance, created, **kwargs):
    if created and not instance.role.exists():  
        try:
            client_role, created = Role.objects.get_or_create(name='client')  
            instance.role.add(client_role)  
            instance.save()
        except Role.DoesNotExist:
            pass


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(
            user=instance,
            username=instance.username,
            email=instance.email,
            name=instance.first_name,
        )


@receiver(post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()


