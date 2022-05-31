from django.urls import path
from . import views

urlpatterns=[
        path('', views.home, name='home'),
        path('login', views.login, name='login'),
        path("register",views.register, name="register"),
        path("forgot_password",views.forgot_password, name="forgot_password"),
        path("send_otp",views.send_otp,name="send otp"),
        path("sampleotp",views.sampleotp,name="sampleotp"),
        path("password_trial",views.password_trial,name="password_trial"),
        path("reset_password",views.reset_password,name="reset_password"),
        path("demo1",views.demo1,name="demo1"),
]