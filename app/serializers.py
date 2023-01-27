from rest_framework import serializers
from .models import Transactions,Device,EmployeeProfile,StaffProfile,Employee,Staff



# class DeviceTransactionsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Transactions
#         fields = '__all__'


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device 
        fields = '__all__'

class DevicedetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device 
        fields = '__all__'

class TransactionsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Transactions
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['username','password']

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['username','password']
