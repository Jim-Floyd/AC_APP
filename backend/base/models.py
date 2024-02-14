from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Position(models.Model):
    position_name = models.CharField(max_length = 20)

class User(AbstractUser):
    username = models.CharField(max_length=200, unique=True, null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")
    position = models.ForeignKey(
        Position, on_delete=models.SET_NULL, null=True, related_name="position_holder"
    )


class Ac_warehouse(models.Model):
    name = models.CharField()
    warehouse_holder = models.ForeignKey(User, on_delete=models.CASCADE)
    model_amount = models.IntegerField()


class Ac_model_brand(models.Model):
    name = models.CharField(max_length = 20)

class Ac_model_type(models.Model):
    name = models.CharField(max_length = 20)

class Ac_model(models.Model):
    model_name = models.CharField(max_length = 50)
    model_brand = models.Foreign_Key(Ac_model_brand, on_delete=models.CASCADE)
    model_type = models.Foreign_Key(Ac_model_type, on_delete=models.CASCADE)
    model_price = models.IntegerField()
    model_margin = models.IntegerField()
    model_dealer_price = models.IntegerField()
    model_warehouse = models.ManyToManyField(Ac_warehouse, related_name="models")


class Ac_payment_type(models.Model):
    name = models.CharField()

class Ac_payment_status(models.Model):
    name = models.CharField()


class Ac_app(models.Model):
    number = models.IntegerField()
    model = models.ManyToManyField(Ac_model, related_name="apps")
    model_amount = models.IntegerField()
    customer_name = models.CharField(max_length = 50)
    customer_phone = models.CharField(max_length = 15)
    customer_address = models.CharField(max_length = 70)
    manager_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="apps")
    delivery_time = models.CharField(max_length = 50)
    delivery_man = models.CharField(max_length = 50)
    payment_type = models.ForeignKey(Ac_payment_type, on_delete=models.CASCADE, related_name="apps")
    payment_status = models.ForeignKey(Ac_payment_status, on_delete=models.CASCADE, related_name="apps")
    warehouse = models.ForeignKey(Ac_warehouse, on_delete=models.CASCADE, related_name="apps")
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_now=True)
    is_canceled = models.BooleanField(default=False)
    canceled_at = models.DateTimeField()
    is_shipped = models.BooleanField(default= False)
    shipped_at = models.DateTimeField()
    is_paid = models.BooleanField(default = False)
    paid_at = models.DateTimeField()















