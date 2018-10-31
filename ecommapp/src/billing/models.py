from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import GuestEmail
User = settings.AUTH_USER_MODEL


class BillingProfileManager(models.Manager):
    def new_or_get(self, request):
        user = request.user
        guest_email_id = request.session.get('guest_email_id')
        created = False
        obj = None
        if user.is_authenticated:
            # if user.email:
            obj, created = self.model.objects.get_or_create(user=user, email=user.email)
        elif guest_email_id is not None:
            guest_email_obj = GuestEmail.objects.get(id=guest_email_id)
            obj, created = self.model.objects.get_or_create(email=guest_email_obj.email)
        else:
            pass
        return obj, created


class BillingProfile(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    email = models.EmailField()
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    objects = BillingProfileManager()

# def billing_profile_created_receiver(sender, instance, *args, **kwargs):
#     if not instance.customer_id and instance.email:
#         print("ACTUAL API REQUEST Send to stripe/braintree")
#         customer = stripe.Customer.create(
#                 email = instance.email
#             )
#         print(customer)
#         instance.customer_id = customer.id

# pre_save.connect(billing_profile_created_receiver, sender=BillingProfile)


@receiver(post_save, sender=User)
def user_created_reciever(sender, instance, created, *args, **kwargs):
    if created and instance.email:
        BillingProfile.objects.get_or_create(
            user=instance, email=instance.email)

# post_save.connect(user_created_reciever, sender=User, weak=False)
