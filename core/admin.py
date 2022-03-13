from django.contrib import admin
from django.conf import settings
from paypalrestsdk import configure
from . import models

configure({
    "mode": settings.PP_MODE,
    "client_id": settings.PP_CL_ID,
    "client_secret": settings.PP_CL_ST
})


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
admin.site.register(models.Courier)
admin.site.register(models.Category)
admin.site.register(models.Job)
admin.site.register(models.Transaction, TransactionAdmin)
