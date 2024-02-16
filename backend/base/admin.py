from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Position)
admin.site.register(models.User)
admin.site.register(models.Ac_model_brand)
admin.site.register(models.Ac_model_type)
admin.site.register(models.Ac_model)
admin.site.register(models.Ac_warehouse)
admin.site.register(models.Ac_payment_type)
admin.site.register(models.Ac_payment_status)
admin.site.register(models.Ac_app)
