from django.contrib import admin, messages
from django.conf import settings
from paypalrestsdk import configure, Payout
import random
import string
from . import models

configure({
    "mode": settings.PP_MODE,
    "client_id": settings.PP_CL_ID,
    "client_secret": settings.PP_CL_ST
})


def payout_to_courier(modeladmin, request, queryset):
    payout_items = []
    transaction_querysets = []

    # get all valid couriers
    for courier in queryset:
        if courier.paypal_email:
            courier_in_transactions = models.Transaction.objects.filter(
                job__courier=courier,
                status=models.Transaction.IN_STATUS
            )

            if courier_in_transactions:
                transaction_querysets.append(courier_in_transactions)
                balance = sum(i.amount for i in courier_in_transactions)
                payout_items.append({
                    "recipient_type": "EMAIL",
                    "amount": {
                        "value": "{:.2f}".format(balance * 0.9),
                        "currency": "USD"
                    },
                    "receiver": courier.paypal_email,
                    "note": "Thank you",
                    "sender_item_id": str(courier.id)
                })

    # payout batch & mail to couriers
    sender_batch_id = ''.join(
        random.choice(string.ascii_uppercase) for i in range(12))
    payout = Payout({
        "sender_batch_header": {
            "sender_batch_id": sender_batch_id,
            "email_subject": "You have received a payment from dparcel"
        },
        "items": payout_items
    })

    # update transaction status to out if success
    try:
        if payout.create():
            for t in transaction_querysets:
                t.update(status=models.Transaction.OUT_STATUS)
            messages.success(request, "Payout[%s] created successfully" % (
                payout.batch_header.payout_batch_id))
        else:
            messages.error(request, payout.error)
    except Exception as e:
        messages.error(request, str(e))


payout_to_courier.short_description = "Payout to couriers"


class CourierAdmin(admin.ModelAdmin):
    list_display = ['user_full_name', 'paypal_email', 'balance', ]
    actions = [payout_to_courier]

    def user_full_name(self, obj):
        return obj.user.get_full_name()

    def balance(self, obj):
        return round(sum(t.amount for t in models.Transaction.objects.filter(job__courier=obj, status=models.Transaction.IN_STATUS)) * 0.9, 2)


class TransactionAdmin(admin.ModelAdmin):
    list_display = [
        'job', 'amount', 'customer', 'courier', 'courier_paypal_email',
        'status',
        'created_at'
    ]
    list_filter = ['status', ]

    def customer(self, obj):
        return obj.job.customer

    def courier(self, obj):
        return obj.job.courier

    def courier_paypal_email(self, obj):
        return obj.job.courier.paypal_email if obj.job.courier else None


# Register your models here.
admin.site.register(models.Customer)
admin.site.register(models.Courier, CourierAdmin)
admin.site.register(models.Category)
admin.site.register(models.Job)
admin.site.register(models.Transaction, TransactionAdmin)
