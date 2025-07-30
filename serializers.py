from rest_framework import serializers
from .models import Customers


class customerserializer(serializers.ModelSerializer):
    class Meta:
        model=Customers
        fields=['id','cust_name','mob','amount']