from rest_framework import serializers, exceptions

from userapp.models import User, Employee


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username","real_name","password","gender")
        extra_kwargs = {
            "username":{
                "required":True,
                "min_length":2,
                "max_length":8,
                "error_messages":{
                    "required":"用户名不能为空",
                    "min_length":"用户名不能低于2个字符",
                    "max_length":"用户名不能超过8个字符",
                }
            },
            "real_name":{
                "write_only":True,
            },
            "gender":{
                "write_only":True
            }
        }

    def validate_pwd(self,value):
        pwd = value.get("password")
        re_pwd = value.pop("re_pwd")
        if pwd != re_pwd:
            raise exceptions.ValidationError('两次密码不一致')
        return value

    def validate(self, attrs):
        username = attrs.get("username")
        user = User.objects.filter(username=username).first()
        if user:
            raise exceptions.ValidationError("用户名已存在")
        return attrs

class EmployeeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("pk","emp_name","img","salary","age","age_change")
        extra_kwargs = {
            "emp_name": {
                "required": True,
                "min_length": 2,
                "max_length": 18,
                "error_messages": {
                    "required": "员工名不能为空",
                    "min_length": "员工名不能低于2个字符",
                    "max_length": "员工名不能超过18个字符",
                }
            },
            "pk":{
                "read_only":True
            },
            "salary":{
                "required":False,
            },
            "age": {
                "required": False,
            }
        }
