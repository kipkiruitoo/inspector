from rest_framework import serializers
from .models import SysUser, Employee


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysUser
        fields = ('user_code', 'username', 'pass_md5')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('emp_no', 'surname', 'o_name')
