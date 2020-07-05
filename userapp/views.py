from django.shortcuts import render
from rest_framework import viewsets
# from rest_framework import generics
# from rest_framework import mixins
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework import status
from .serializers import UserModelSerializer,EmployeeModelSerializer
from userapp.models import User, Employee
from utils.response import APIResponse

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter()
    serializer_class = UserModelSerializer

    def register(self, request, *args, **kwargs):
        response = self.create(request, *args, **kwargs)
        if response:
            return APIResponse(status.HTTP_200_OK, True, results=response.data)
        return APIResponse(status.HTTP_500_INTERNAL_SERVER_ERROR, "注册失败")

    def login(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        # print(username,password)
        user_obj = User.objects.filter(username=username, password=password).first()
        # print(user_obj)
        if user_obj:
            return APIResponse(status.HTTP_200_OK, True, results=UserModelSerializer(user_obj).data)
        return APIResponse(status.HTTP_500_INTERNAL_SERVER_ERROR, "登陆失败")

class EmployeeGenericAPIView(ListModelMixin,
                             CreateModelMixin,
                             RetrieveModelMixin,
                             UpdateModelMixin,
                             DestroyModelMixin,
                             GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer
    # lookup_field = 'id'
    def get(self,request,*args,**kwargs):
        emp_id = kwargs.get("pk")
        print(emp_id)
        if emp_id:
            emp = self.retrieve(request,*args,**kwargs)
            return APIResponse(status.HTTP_200_OK, True, results=emp.data)
        else:
            emp_list = self.list(request,*args,**kwargs)
            print(emp_list)
            return APIResponse(status.HTTP_200_OK,True,results=emp_list.data)

    def post(self,request,*args,**kwargs):
        emp_obj = self.create(request,*args,**kwargs)
        return APIResponse(status.HTTP_200_OK,True,results=emp_obj.data)

    def put(self,request,*args,**kwargs):
        emp_obj = self.update(request, *args, **kwargs)
        return APIResponse(status.HTTP_200_OK, True, results=emp_obj.data)

    def delete(self,request,*args,**kwargs):
        emp_obj = self.destroy(request, *args, **kwargs)
        print(emp_obj)
        return APIResponse(status.HTTP_200_OK, True)