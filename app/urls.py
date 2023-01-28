from django.urls import path,include
from .views import EmployeeListCreateView,StaffListCreateView,DeviceListCreateView,TransactionListCreateView,DevicedetailView,Transactiondevice

urlpatterns = [
    # TO SEE ALL TRANSACTION MADE ON ALL SORTS OF DEVICES
    path('transaction/',TransactionListCreateView.as_view()),
    # TO SEE ALL TRANSACTION ON ON SINGLE DEVICE SPECIFIED BY ID
    path('transaction/device/<int:pk>/',Transactiondevice.as_view()),
    # TO SEE ALL AVAILABLE DEVICES AND CREATE NEW ONE
    path('device/',DeviceListCreateView.as_view()),
    # TO SEE AND UPDATE DETAIKLS OF A DEVICE
    path('device/<int:pk>/',DevicedetailView.as_view()),
    # CREATE STAFF USERS
    path('staff/',StaffListCreateView.as_view()),
    # CREATE EMPLOYEE 
    path('employee/',EmployeeListCreateView.as_view()),
    # THERE IS A SMALL PROBLEM HERE LIKE WHEN ADDING TRANSACTION STAFF USER MAY MISTAKENLY SELECT EMPLOYEE
    # FROM OTHER COMPANY WHICK I COULD NOT FIX
    # TO LOG IN GO TO api/auth/login AND ONLY STAFF MEMBER MAKE TRANSACTIONS
    #  
]