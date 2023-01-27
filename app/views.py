from rest_framework.generics import ListCreateAPIView,UpdateAPIView,ListAPIView,RetrieveAPIView
from .models import Transactions,Device,Staff,Employee
from .serializers import TransactionsSerializer,EmployeeSerializer
from .serializers import  StaffSerializer,DeviceSerializer


class Transactiondevice(ListAPIView):
    queryset  = Transactions.objects.all()
    serializer_class = TransactionsSerializer

  
    
    def get(self,request,*args,**kwargs):
     
        self.queryset = self.queryset.filter(Device_id=kwargs['pk'])
        ret =  super().get(self,request,*args,**kwargs)
        # ret = ret.filter(id=kwargs['pk'])
        return ret
    

class TransactionListCreateView(ListCreateAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer

class DeviceListCreateView(ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DevicedetailView(UpdateAPIView,RetrieveAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class StaffListCreateView(ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class EmployeeListCreateView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


