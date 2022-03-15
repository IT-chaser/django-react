from rest_framework import serializers
from my_model.models import MyProduct

class MyProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyProduct
        fields = ('id',
                  'name',
                  'product_code',
                  'visibility',
                  'currency_type',
                  'price',
                  'requester_ip',
                  'created_date')