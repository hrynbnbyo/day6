from django.db import models


# Create your models here.

class Department(models.Model):
    dept_name = models.CharField(max_length=20)

    class Meta:
        db_table = 'dept'

class Employee(models.Model):
    emp_name = models.CharField(max_length=30)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    age = models.IntegerField()
    photo = models.ImageField(upload_to="img", default="img/1.jpg")
    dept = models.ForeignKey(to="Department", on_delete=models.CASCADE, null=True, blank=True)

    @property
    def dept_name(self):
        return self.dept.dept_name

    class Meta:
        db_table = "bz_employee"
        verbose_name = "员工"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.emp_name
