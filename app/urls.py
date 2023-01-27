from django.urls import path,include
from .views import EmployeeListCreateView,StaffListCreateView,DeviceListCreateView,TransactionListCreateView,DevicedetailView,Transactiondevice

urlpatterns = [
    path('transaction/',TransactionListCreateView.as_view()),
    path('transaction/device/<int:pk>/',Transactiondevice.as_view()),
    path('device/',DeviceListCreateView.as_view()),
    path('device/<int:pk>/',DevicedetailView.as_view()),
    path('staff/',StaffListCreateView.as_view()),
    path('employee/',EmployeeListCreateView.as_view()),
]