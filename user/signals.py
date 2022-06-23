from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from customer.models import Customer


@receiver(post_save, sender=User)
def created_profile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)
        print("Profile created")

@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.customer.save()
        print("Update Profile")