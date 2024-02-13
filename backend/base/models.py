from django.db import models

# Create your models here.

class Ac_app(models.Model):
    number = models.IntegerField()
    model_name = models.ForeignKey()
    model_amount = models.IntegerField()
    customer_name = models.CharField(max_length = 50)
    customer_phone = models.CharField(max_length = 15)
    customer_address = models.CharField(max_length = 70)
    manager_id = models.ForeignKey()
    delivery_time = models.CharField(max_length = 50)
    delivery_man = models.CharField(max_length = 50)
    payment_type = models.ForeignKey()
    payment_status = models.ForeignKey()
    warehouse = models.ForeignKey()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_now=True)
    is_canceled = models.BooleanField(default=False)
    canceled_at = models.DateTimeField()
    is_shipped = models.BooleanField(default= False)
    shipped_at = models.DateTimeField()
    is_paid = models.BooleanField(default= False)
    paid_at = models.DateTimeField()


class Ac_warehouse(models.Model):
    name = models.CharField()
    warehouse_holder = models.ForeignKey()

class Ac_model(models.Model):
    model_name = models.CharField(max_length = 50)
    model_brand = models.Foreign_Key()
    model_type = models.Foreign_Key()
    model_price = models.IntegerField()
    model_margin = models.IntegerField()
    model_dealer_price = models.IntegerField()
    model_warehouse = models.ManyToManyField(Ac_warehouse)


class Ac_model_brand(models.Model):
    name = models.CharField(max_length = 20)

class Ac_model_type(models.Model):
    name = models.CharField(max_length = 20)

class Ac_manager(models.Model):
    pass


class Ac_payment_type(models.Model):
    name = models.CharField()

class Ac_payment_status(models.Model):
    name = models.CharField()



