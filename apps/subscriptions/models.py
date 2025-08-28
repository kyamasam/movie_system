from django.db import models
from apps.core.models import BaseModel
from apps.users.models import User

class SubscriptionPackage(BaseModel):
    name = models.CharField(max_length=100)
    price_monthly = models.DecimalField(max_digits=10, decimal_places=2)
    price_yearly = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_devices = models.IntegerField()

    def __str__(self):
        return self.name


class Subscription(BaseModel):
    subscription_package = models.ForeignKey(SubscriptionPackage, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)


class Payment(BaseModel):
    PAYMENT_METHODS = [
        ("mpesa", "Mpesa"),
        ("card", "Card"),
    ]
    PAYMENT_STATUS = [
        ("completed", "Completed"),
        ("failed", "Failed"),
        ("pending", "Pending"),
    ]

    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    confirmation_code = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField()
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
