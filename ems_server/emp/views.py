from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, \
    RetrieveModelMixin

# 继承哪个视图类合适
from emp.models import Employee, Department
from emp.serializer import EmployeeModelSerializer, DeptModelSerializer
from utils.response import APIResponse


class EmployeeAPIView(ListModelMixin
                        ,RetrieveModelMixin
                        ,CreateModelMixin
                        ,DestroyModelMixin
                        ,UpdateModelMixin
                        ,GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer

    def get(self, request, *args, **kwargs):
        if "pk" in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def patch(self,request,*args,**kwargs):
        response = self.partial_update(request, *args, **kwargs)
        return APIResponse(results=response.data)



class DepartmentAPIView(ListModelMixin, GenericAPIView):
    queryset = Department.objects.all()
    serializer_class = DeptModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
