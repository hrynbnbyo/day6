from rest_framework.serializers import ModelSerializer

from emp.models import Employee, Department


class EmployeeModelSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ["id", "emp_name", "salary", "age", "photo", "dept", "dept_name"]


class DeptModelSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = ["id", "dept_name"]



