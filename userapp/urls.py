from django.urls import path

from userapp import views

urlpatterns = [
    path('login/',views.UserViewSet.as_view({'post':'login'})),
    path('register/',views.UserViewSet.as_view({'post':'register'})),
    path('emp/',views.EmployeeGenericAPIView.as_view()),
    path('emp/<str:pk>/',views.EmployeeGenericAPIView.as_view()),
]