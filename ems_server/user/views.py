from rest_framework.views import APIView

from emp.models import Employee
from user.models import Admin
from user.serializer import AdminModelSerializer
from utils.response import APIResponse


class AdminAPIView(APIView):

    def get(self, request, *args, **kwargs):
        """
        用户登录请求的处理
        :return: 登录成功与否 用户的信息
        """
        name = request.GET.get("name")
        password = request.GET.get("password")

        admin_obj = Admin.objects.filter(name=name, password=password).first()
        print(admin_obj)
        if admin_obj:
            data = AdminModelSerializer(admin_obj).data
            return APIResponse(200, True, results=data)

        return APIResponse(http_status=400)

    def post(self, request, *args, **kwargs):
        """
        用户的注册请求
        :return: 返回注册成功的用户
        """
        request_data = request.data
        serializer = AdminModelSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        admin_obj = serializer.save()

        if admin_obj:
            return APIResponse(200, True, results=AdminModelSerializer(admin_obj).data)
        return APIResponse(400, data_message="您提交的注册信息有误")

    def delete(self, request, *args, **kwargs):
        id = request.GET.get('id')
        emp_obj = Employee.objects.filter(id=id)
        if emp_obj:
            emp_obj.delete()
            emp_obj2 = Employee.objects.filter(id=id)
            if emp_obj2:
                return APIResponse(400,"删除失败")
            return APIResponse(200,"删除成功")

