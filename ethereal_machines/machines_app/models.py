# machines_app/models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, employee_id, password=None, role=None):
        if not employee_id:
            raise ValueError('Users must have an employee ID')
        user = self.model(employee_id=employee_id, role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, employee_id, password=None, role=None):
        user = self.create_user(employee_id, password=password, role=role)
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    employee_id = models.CharField(max_length=50, unique=True)
    password_hash = models.CharField(max_length=128)
    role = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'employee_id'
    REQUIRED_FIELDS = []


class Machine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    acceleration = models.FloatField()
    velocity = models.FloatField()

    def __str__(self):
        return self.name

class DynamicData(models.Model):
    id = models.AutoField(primary_key=True)
    machine_id = models.ForeignKey(Machine, related_name='dynamic_data', on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    actual_position_x = models.FloatField(null=True, blank=True, default=None)
    actual_position_y = models.FloatField(null=True, blank=True, default=None)
    actual_position_z = models.FloatField(null=True, blank=True, default=None)
    actual_position_a = models.FloatField(null=True, blank=True, default=None)
    actual_position_c = models.FloatField(null=True, blank=True, default=None)
    distance_to_go_x = models.FloatField(null=True, blank=True, default=None)
    distance_to_go_y = models.FloatField(null=True, blank=True, default=None)
    distance_to_go_z = models.FloatField(null=True, blank=True, default=None)
    distance_to_go_a = models.FloatField(null=True, blank=True, default=None)
    distance_to_go_c = models.FloatField(null=True, blank=True, default=None)
    homed_x = models.BooleanField()
    homed_y = models.BooleanField()
    homed_z = models.BooleanField()
    homed_a = models.BooleanField()
    homed_c = models.BooleanField()
    tool_offset_x = models.FloatField(null=True, blank=True, default=None)
    tool_offset_y = models.FloatField(null=True, blank=True, default=None)
    tool_offset_z = models.FloatField(null=True, blank=True, default=None)
    tool_offset_a = models.FloatField(null=True, blank=True, default=None)
    tool_offset_c = models.FloatField(null=True, blank=True, default=None)
    created_by = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Data for {self.machine.name} by {self.created_by}"