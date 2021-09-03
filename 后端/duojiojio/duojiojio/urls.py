"""duojiojio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from sellm import views

urlpatterns = [
    # # 1.用于显示菜单
    # url(r'^Test', views.Test),
    # # 2.用于显示订单
    # url(r'^getOrderTest', views.getOrderTest),
    # # 3.用于添加订单中的添加每个菜品项目
    # url(r'^setitemtest', views.SetItemTest),
    # # 用于增加订单
    # url(r'^setordertest', views.SetOrderTest),
    # # 5.用于得到地址（所有）
    # url(r'^getadressestest', views.getAddressesTest),
    # # 6.用于得到地址（一条）来初始化编辑该地址页面
    # url(r'^getadresstest', views.getAddressTest),
    # # 6.用于编辑一条地址
    # url(r'^setadresstest', views.setAddressTest),
    # # 7.用于登录
    # url(r'^logintest', views.LoginTest),
    # # 8.用于注册
    # url(r'^registertest', views.RegisterTest),
    # 店家展览图
    url(r'^viewforseller', views.viewforseller),
    url(r'^getUserInfo',views.getUserInfo1),
    url(r'^setUserInfo',views.setUserInfo1),
    # viewforsellertodo店家菜单展示
    url(r'^viewtodo', views.viewtodo),
    #addmenu 店家上菜
    url(r'^addmenu',views.addmenu),
    #deleteMenu 店家删菜
    url(r'^deleteMenu',views.deleteMenu),
    #店家用户信息获取usersinfo
    url(r'^usersinfo',views.usersinfo),
    #altermenu店家修改菜的信息
    url(r'^altermenu', views.altermenu),
    #deluser删除用户
    url(r'^deluser', views.deluser),
    #alteruser改变用户信息商家
    url(r'^alteruser', views.alteruser),
    #商家接单信息ordertobegin
    url(r'^ordertobegin', views.ordertobegin),
    #商家开始接单
    url(r'^beginoder', views.beginoder),
    #商家待完成信息ordertofinish
    url(r'^ordertofinish', views.ordertofinish),
    #商家完成订单
    url(r'^finishoder', views.finishoder),
    #orderall 商家获取所有人订单
    url(r'^orderall', views.orderall),
    path('admin/', admin.site.urls),
    path('api/', views.Test1),
    path('apii/', views.getOrderTest1),
    path('setitemtest/', views.SetItemTest1),
    path('setordertest/', views.SetOrderTest1),
    path('getadresstest/', views.getAddressTest1),
    path('setadresstest/', views.setAddressTest1),
    path('addadresstest/', views.addAddressTest1),
    path('getadressestest/', views.getAddressesTest1),
    path('logintest/', views.LoginTest1),
    path('registertest/', views.RegisterTest1),
    path('getuserInfo/', views.getUserInfo1),
    path('setuserInfo/', views.setUserInfo1),
    path('deleteadresstest/', views.deleteAddressTest1),
    path('deleteordertest/', views.deleteOrderTest1)
]
