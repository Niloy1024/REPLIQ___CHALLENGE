from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

class Company(models.Model):
    name = models.CharField(max_length=20,default='')

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        Employee = "Employee", "Employee"
        Staff  = "Staff", "Staff"

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


class EmployeeManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.Employee)


class Employee(User):

    base_role = User.Role.Employee
    is_staff = True
    Employee = EmployeeManager()

    class Meta:
        proxy = True


@receiver(post_save, sender=Employee)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "Employee":
        EmployeeProfile.objects.create(user=instance)


class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.IntegerField(null=True, blank=True)


class StaffManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.Staff)


class Staff(User):

    base_role = User.Role.Staff

    Staff = StaffManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for teachers"


class StaffProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher_id = models.IntegerField(null=True, blank=True)


@receiver(post_save, sender=Staff)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "Staff":
        StaffProfile.objects.create(user=instance)

class Device(models.Model):
    choices  = [
        ('Mobile', 'Mobile_phn'),
        ('Computer', 'Computer'),
        ('Printer', 'Printer'),
    ]
    device_type = models.CharField(max_length=20,choices=choices)
    state_choices  = [
        ('OFF', 'Malfunctioned'),
        ('SEMI_OFF', 'Need_to_be_Fixed'),
        ('ON', 'WORKING'),
    ]
    device_state = models.CharField(max_length=20,choices=state_choices)

    
    

class Transactions(models.Model):
    choices  = [
        ('Render', 'Render'),
        ('Receive', 'Receive'),
    ]
    state_choices  = [
        ('OFF', 'Malfunctioned'),
        ('SEMI_OFF', 'Need_to_be_Fixed'),
        ('ON', 'WORKING'),
    ]
    Device = models.ForeignKey(Device,on_delete=models.CASCADE)
    Employee = models.ForeignKey(EmployeeProfile,on_delete=models.CASCADE)
    Staff = models.ForeignKey(StaffProfile,on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10,choices=choices)
    time =  datetime.now()
    device_condition = models.CharField(max_length=10,choices=state_choices)

@receiver(post_save, sender=Transactions)
def create_user_profile(sender, instance, created, **kwargs):
    if created :
        instance.device_condition = instance.Device.device_state

    