from rest_framework import serializers
from . import models



class Ac_appSerializier(serializers.ModelSerializer):
    class Meta:
        model = models.Ac_app
        fields = "__all__"

class PositionSerializier(serializers.ModelSerializer):
    class Meta:
        model = models.Position
        fields = "__all__"

class UserSerializier(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = "__all__"


class Ac_model_brandSerializier(serializers.ModelSerializer):
    class Meta:
        model = models.Ac_model_brand
        fields = "__all__"


class Ac_model_typeSerializier(serializers.ModelSerializer):
    class Meta:
        model = models.Ac_model_type
        fields = "__all__"



class Ac_modelSerializier(serializers.ModelSerializer):
    class Meta:
        model = models.Ac_model
        fields = "__all__"


class Ac_warehouseSerializier(serializers.ModelSerializer):
    class Meta:
        model = models.Ac_warehouse
        fields = "__all__"


class Ac_Ac_payment_typeSerializier(serializers.ModelSerializer):
    class Meta:
        model = models.Ac_payment_type
        fields = "__all__"

class Ac_payment_statusSerializier(serializers.ModelSerializer):
    class Meta:
        model = models.Ac_payment_status
        fields = "__all__"

    