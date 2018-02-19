from rest_framework import serializers
from .models import BeeMerch

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeeMerch
        fields = ('id','name','description','price')
