from rest_framework import serializers
from .models import Transactions,Device,EmployeeProfile,StaffProfile,Employee,Staff,Company




class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device 
        fields = '__all__'

class DevicedetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device 
        fields = '__all__'

class TransactionsSerializer(serializers.ModelSerializer):
    # hell  = serializers.PrimaryKeyRelatedField(queryset = Company.objects.all()  ,many=True)
    
    class Meta:
        model = Transactions
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    # hell  = serializers.PrimaryKeyRelatedField(queryset = Company.objects.all()  ,many=True)
    class Meta:
        model = Employee
        fields = ['username','password','company']


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['username','password','company']

