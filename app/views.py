from rest_framework.generics import ListCreateAPIView,UpdateAPIView,ListAPIView,RetrieveAPIView
from .models import Transactions,Device,Staff,Employee
from .serializers import TransactionsSerializer,EmployeeSerializer
from .serializers import  StaffSerializer,DeviceSerializer
from django.contrib.auth.hashers import make_password


class Transactiondevice(ListAPIView):
    queryset  = Transactions.objects.all()
    serializer_class = TransactionsSerializer
    
    def get(self,request,*args,**kwargs):
        self.queryset = self.queryset.filter(Device_id=kwargs['pk'])
        ret =  super().get(self,request,*args,**kwargs)
        return ret
    

class TransactionListCreateView(ListCreateAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer

    def get(self,c,*x,**y):
        print(self)
        print(c.user.company)
        return super().get(self,c,*x,**y)

class DeviceListCreateView(ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DevicedetailView(UpdateAPIView,RetrieveAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class StaffListCreateView(ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    def create(f,s,*c,**d):
        print('create')
        return super().create(s,*c,**d)

    def perform_create(f,s,*c,**d):
        password =  make_password( s.validated_data['password'])
        s.validated_data.pop('password')
        s.validated_data['password']=password 
        i=s.save()

class EmployeeListCreateView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def perform_create(f,s,*c,**d):
        password =  make_password( s.validated_data['password'])
        s.validated_data.pop('password')
        s.validated_data['password']=password 
        i=s.save()


