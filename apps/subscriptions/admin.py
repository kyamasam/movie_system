from django.contrib import admin
from .models import SubscriptionPackage, Subscription, Payment

@admin.register(SubscriptionPackage)
class SubscriptionPackageAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price_monthly", "price_yearly", "number_of_devices")
    search_fields = ("name",)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "subscription_package", "start_date", "end_date", "is_active")
    list_filter = ("is_active", "start_date", "end_date")
    search_fields = ("user__first_name", "user__last_name")


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "subscription", "amount_paid", "payment_status", "payment_method", "payment_date")
    list_filter = ("payment_status", "payment_method", "payment_date")
    search_fields = ("confirmation_code", "user__first_name", "user__last_name")
