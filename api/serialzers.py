from rest_framework.serializers import ModelSerializer
from employee_register.models import Employee


class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ['fullname', 'emp_code', 'mobile', 'position']
