from rest_framework import exceptions
from rest_framework.serializers import ModelSerializer

from user.models import Admin


class AdminModelSerializer(ModelSerializer):
    class Meta:
        model = Admin
        fields = "__all__"

        extra_kwargs = {
            "name": {
                'required': True,
                "min_length": 2,
                "error_messages": {
                    'required': "用户名必填",
                    "min_length": "长度太短了"
                }
            }
        }

    # 用户名重复  两次密码不一致
    def validate_name(self, value):
        admin = Admin.objects.filter(name=value).first()
        if admin:
            raise exceptions.ValidationError("用户名已存在")

        return value

    def validate(self, attrs):
        # 完成两次密码是否一致的验证
        return attrs
