from django.db import models

from billing.models import BillingProfile
# Create your models here.

ADDRESS_TYPES =(
    ('billing', 'Billing'),
    ('shipping', 'Shipping'),
)
class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile, on_delete=models.CASCADE)
    address_type = models.CharField(max_length = 180, choices = ADDRESS_TYPES)
    address_line_1 = models.CharField(max_length = 180)
    address_line_2 = models.CharField(max_length = 180)
    city = models.CharField(max_length = 180)
    country = models.CharField(max_length = 180, default='India')
    state = models.CharField(max_length = 180)
    postal_code = models.CharField(max_length = 180)

    def __str__(self):
        return str(self.billing_profile)
    
    def get_address(self):
        return "{line1}\n{line2}\n{city}\n{state}, {postal}\n{country}".format(line1 = self.address_line_1, line2 = self.address_line_2 or "",city = self.city,state = self.state,postal= self.postal_code,country = self.country)

    class Meta:
        verbose_name = 'address'
        verbose_name_plural = 'addresses'
