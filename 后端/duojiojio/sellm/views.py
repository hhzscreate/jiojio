from django.shortcuts import render

# Create your views here.
import datetime

import requests

from django.shortcuts import render
from rest_framework.decorators import api_view

from sellm import models
from django.http import HttpResponse
import json
from sellm.models import DiskTest, Images, OrderTest, ItemTest, AddressItemTest, UserTest, UserInfo, MenuTest
from django.forms.models import model_to_dict
import redis
from django.shortcuts import render
from django.shortcuts import redirect

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
import json
import datetime


@api_view(['GET'])
def Test1(request):
    queryset = models.MenuTest.objects.all()  # 得到左侧的所有菜单
    data = []  # 最终要返回的数据
    # 挨个把他转换成json格式
    for i in queryset:  # 对面每一个菜单项，都是一个字典 p_temp

        menuId = i.menuId  # 取得当前一栏的id比如盖饭的id

        products = []  # 取得当前菜单里的所有的products！
        # products=DiskTest.objects.filter(disk_id=menuId)  # 红色的是数据库上的名字
        for m in DiskTest.objects.filter(category_id=menuId):  # m是category_id与menuId相同的一个菜品

            temp = Images.objects.get(disk_id=m.disk_id)  # 每个菜品有一个disk_id，用来找两张图片
            images = [
                {
                    "url": temp.url_0
                },
                {
                    "url": temp.url_1
                }
            ]

            # p_temp_0 是一个完整的菜品字典，而一份菜单中有很多这样的菜品
            p_temp_0 = {
                "id": m.disk_id,
                "name": m.name,
                "description": m.description,
                "category_id": m.category_id,
                "support_takeaway": m.support_takeaway,
                "images": images,
                "sort": m.sort,
                "price": m.price
            }
            products.append(p_temp_0)
        p_temp = {
            "id": i.menuId,
            "name": i.name,
            "products": products,
            "sort": i.sort
        }
        data.append(p_temp)
    return HttpResponse(json.dumps({"status": 200, "msg": "OK!", "data": data}, ensure_ascii=False),
                        content_type="application/json")


@api_view(['GET'])
def getOrderTest1(request):
    data = []  # 需要找出一个人的所有订单    一份订单一个id，是一个字典，同时一份订单中的items也是一个字典
    # userName=request.GET.get("userName")
    openId = request.GET.get("openId")
    userName = "Tang"  # 暂时用静态数据
    id = 1
    orderlist = OrderTest.objects.filter(openId=openId)
    for m in orderlist:
        items = []
        for i in ItemTest.objects.filter(orderId=m.orderId):
            # 装菜品
            p_temp = {
                "quantity": i.quantity,
                "total_fee": '%.2f' % (i.total_fee),
                "price": i.price,
                "sname": i.sname,
                "image": i.image
            }
            items.append(p_temp)
        if m.state==0:
            message='待接单'
        elif m.state==1:
            message='待完成'
        else:
            message='已完成'
        p_temp_0 = {
            "id": id,  # 表示这是这个人的第几份订单
            "total_fee": '%.2f' % (m.total_fee),
            "payment": '%.2f' % (m.payment),
            "created_at": m.created_at,
            "remarks": m.remarks,
            "shopName": m.shopName,
            "items": items,
            "orderId": m.orderId,
            'state':m.state,
            'message':message
        }
        id = id + 1
        data.append(p_temp_0)
    return HttpResponse(json.dumps({"status": 200, "msg": "OK!", "data": data}, ensure_ascii=False),
                        content_type="application/json")


def deleteOrderTest1(request):
    orderId = request.GET.get("orderId")
    openId = request.GET.get("openId")

    # 找到这一份订单
    order_delete = OrderTest.objects.get(openId=openId, orderId=orderId)
    # 首先删除与该订单有关的所有item
    itemlist = ItemTest.objects.filter(openId=openId, orderId=orderId)
    if (itemlist):
        for m in itemlist:
            m.delete()

    if (order_delete):
        order_delete.delete()

    return HttpResponse(json.dumps({"status": 200, "msg": "OK!", "data": ""}, ensure_ascii=False),
                        content_type="application/json")


def SetItemTest1(request):  # 装入数据库
    item = ItemTest()  # 生成对象
    # 其实这里最好加一个openId的数据项，找的更加准确
    # 否则就要确保orderId的唯一性
    queryset = ItemTest.objects.all()
    id=2
    for i in queryset:
        id = max(i.id, id)
    id = id + 1
    orderId = request.GET.get("orderId")  # 是订单号，一般是唯一的
    sname = request.GET.get("sname")
    quantity = int(request.GET.get("quantity"))
    Disk = DiskTest.objects.get(name=sname)  # 价从数据库里找该菜品的完整信息
    price_int = int(Disk.price)
    total_fee = price_int * quantity  # 后台计算总价即可
    image = Images.objects.get(disk_id=Disk.disk_id)  # 完整信息
    #   create_at=datetime.datetime.now().strftime('%Y%m%d%H%M%S')  #字符串的创建时间

    item.sname = sname
    item.quantity = quantity
    item.orderId = orderId
    item.image = image.url_0
    item.price = Disk.price
    item.total_fee = total_fee
    item.id=id
    item.save()  # 存入数据库

    return HttpResponse(json.dumps({"status": 200, "msg": "OK!", "data": ""}, ensure_ascii=False),
                        content_type="application/json")


def SetOrderTest1(request):
    queryset=OrderTest.objects.all()
    id = 2
    for i in queryset:
        id = max(i.id, id)
    id = id + 1
    openId = request.GET.get("openId")
    ordertest = OrderTest()
    total_fee = request.GET.get("total_fee")
    remarks = request.GET.get("remarks")
    payment = request.GET.get("payment")
    orderId = request.GET.get("orderId")
    userName = request.GET.get("userName")
    # create_at=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    create_at = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
    ordertest.id=id
    ordertest.total_fee = total_fee
    ordertest.remarks = remarks
    ordertest.payment = payment
    ordertest.orderId = orderId
    ordertest.shopName = "来福士店"
    ordertest.created_at = create_at
    ordertest.userName = userName
    ordertest.openId = openId
    ordertest.state=0
    ordertest.save()

    return HttpResponse(json.dumps({"status": 200, "msg": "OK!", "data": ""}, ensure_ascii=False),
                        content_type="application/json")


@api_view(['GET'])
def getAddressesTest1(request):
    user_id = request.GET.get('user_id')
    addresseslist = AddressItemTest.objects.filter(user_id=user_id)
    data = []
    for m in addresseslist:
        p_temp_0 = {
            "id": m.id,
            "user_id": m.user_id,
            "name": m.name,
            "phone": m.phone,
            "gender": m.gender,
            "address": m.address,
            "complete_address": m.complete_address,
            "description": m.description,
            "latitude": m.latitude,
            "longitude": m.longitude,
            "is_default": m.is_default
        }
        data.append(p_temp_0)
    return HttpResponse(json.dumps({"status": 200, "msg": "OK!", "data": data}, ensure_ascii=False),
                        content_type="application/json")


# 取得单独的一条地址进行修改
@api_view(['GET'])
def getAddressTest1(request):
    user_id = request.GET.get('user_id')
    id = request.GET.get('id')  # 这个人的哪个
    address = AddressItemTest.objects.get(user_id=user_id, id=id)
    # 先找到是哪个人的，然后找到里面具体的，也可以同时找
    data = {
        "id": address.id,
        "user_id": address.user_id,
        "name": address.name,
        "phone": address.phone,
        "gender": address.gender,
        "address": address.address,
        "complete_address": address.complete_address,
        "description": address.description,
        "latitude": address.latitude,
        "longitude": address.longitude,
        "is_default": address.is_default
    }
    return HttpResponse(json.dumps({"status": 200, "msg": "OK!", "data": data}, ensure_ascii=False),
                        content_type="application/json")


def setAddressTest1(request):
    user_id = request.GET.get('user_id')
    id = request.GET.get('id')
    name = request.GET.get('name')
    phone = request.GET.get('phone')
    address = request.GET.get('address')
    complete_address = request.GET.get('complete_address')
    description = request.GET.get('description')
    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')
    is_default = request.GET.get('is_default')
    gender = request.GET.get('gender_0')  # 不知为什么变成了bool型
    # gender=0
    # if(gender_bool):
    #     gender=1
    if (is_default):  # 如果默认地址被修改了，则需要遍历
        for m in AddressItemTest.objects.all():
            m.is_default = 0
            m.save()

    addressItem = AddressItemTest.objects.get(user_id=user_id, id=id)
    addressItem.name = name
    addressItem.phone = phone
    addressItem.gender = gender
    addressItem.address = address
    addressItem.complete_address = complete_address
    addressItem.description = description
    addressItem.latitude = latitude
    addressItem.longitude = longitude
    addressItem.is_default = is_default
    addressItem.save()
    return HttpResponse(json.dumps({"status": 200, "msg": "OK!", "data": " "}, ensure_ascii=False),
                        content_type="application/json")


# 删除一条记录
def deleteAddressTest1(request):
    user_id = request.GET.get('user_id')
    id = request.GET.get('id')
    addressItem = AddressItemTest.objects.get(user_id=user_id, id=id)
    addressItem.delete()
    return HttpResponse(json.dumps({"status": 200, "msg": "OK!", "data": " "}, ensure_ascii=False),
                        content_type="application/json")


def addAddressTest1(request):
    user_id = request.GET.get('user_id')

    name = request.GET.get('name')
    phone = request.GET.get('phone')
    address = request.GET.get('address')
    complete_address = request.GET.get('complete_address')
    description = request.GET.get('description')
    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')
    is_default = request.GET.get('is_default')
    gender = request.GET.get('gender')

    if (is_default):  # 如果默认地址被修改了，则需要遍历
        for m in AddressItemTest.objects.all():
            m.is_default = 0
            m.save()

    addressItem = AddressItemTest()
    id=2
    queryset=AddressItemTest.objects.all()
    for i in queryset:
        id=max(i.id,id)
    id=id+1
    addressItem.id=id
    addressItem.user_id = user_id
    addressItem.name = name
    addressItem.phone = phone
    addressItem.gender = gender
    addressItem.address = address
    addressItem.complete_address = complete_address
    addressItem.description = description
    addressItem.latitude = latitude
    addressItem.longitude = longitude
    addressItem.is_default = is_default
    addressItem.save()
    return HttpResponse(json.dumps({"status": 200, "msg": "OK!", "data": " "}, ensure_ascii=False),
                        content_type="application/json")


def LoginTest1(request):
    userId = request.GET.get('userId')
    password = request.GET.get('password')
    usertest = UserTest.objects.get(userId=userId, password=password)
    # userName=usertest.userName
    print(usertest.userId)
    data=[]
    if (usertest):  # 如果找到了
        temp = {
            "userId": usertest.userId,
            "userName": usertest.userName,
        }
        data.append(temp)
        return HttpResponse(json.dumps({"status": 1, "msg": "OK!", "data": data}, ensure_ascii=False),
                            content_type="application/json")
    else:
        return HttpResponse(json.dumps({"status": 0, "msg": "OK!", "data": ""}, ensure_ascii=False),
                            content_type="application/json")


def RegisterTest1(request):
    userId = request.GET.get('userId')
    password = request.GET.get('password')
    userName = "默认名字"
    user =UserTest.objects.filter(userId=userId)
    if len(user)>0:
        return HttpResponse(json.dumps({"status": 0, "msg": "注册失败!", "data": ""}, ensure_ascii=False),
                            content_type="application/json")
    id=2
    queryset=UserTest.objects.all()
    for i in queryset:
        id=max(i.id,id)
    id=id+1
    usernew = UserTest()
    usernew.userName = userName
    usernew.userId = userId
    usernew.password = password
    usernew.id=id
    usernew.save()

    # 塞入一条默认的userinfo
    id = 2
    queryset = UserInfo.objects.all()
    for i in queryset:
        id = max(i.id, id)
    id = id + 1
    new = UserInfo()
    new.id=id
    new.userId = userId
    # 默认生日，默认地址
    new.birthday = "2000-01-01"
    new.url = "https://wx.qlogo.cn/mmopen/vi_32/vM0qx5z4BQUQU4icZNct8Oib0Q0ypMW6hdhejkBxrTzibvYHtdyaQI85hsWvL6PoA3ic3Jjwn99YdfxEj1ib7gvaJeQ/132"
    new.telphone = ""
    new.username = "默认名字"
    new.gender = 0
    new.save()

    return HttpResponse(json.dumps({"status": 1, "msg": "OK!", "data": ""}, ensure_ascii=False),
                        content_type="application/json")


def getUserInfo1(request):
    userId = request.GET.get('userId')
    userinfo = UserInfo.objects.get(userId=userId)

    # 找不到是因为登录的时候应该塞一个默认的userinfo进去
    if (userinfo):
        data = {
            "username": userinfo.username,
            "telphone": userinfo.telphone,
            "gender": userinfo.gender,
            "birthday": userinfo.birthday,
            "url": userinfo.url
        }
    else:
        data = {}

    return HttpResponse(json.dumps({"status": 1, "msg": "OK!", "data": data}, ensure_ascii=False),
                        content_type="application/json")


def setUserInfo1(request):
    username = request.GET.get('username')
    birthday = request.GET.get('birthday')
    gender = request.GET.get('gender')
    telphone = request.GET.get('telphone')
    userId = request.GET.get('userId')
    # url=request.GET.get('url')
    userinfo = UserInfo.objects.get(userId=userId)
    user = UserTest.objects.get(userId=userId)

    if (userinfo):
        userinfo.username = username
        userinfo.birthday = birthday
        userinfo.gender = gender
        userinfo.telphone = telphone
        # userinfo.url=url
        userinfo.save()

        user.userName = username
        user.save()
    return HttpResponse(json.dumps({"status": 1, "msg": "OK!", "data": ""}, ensure_ascii=False),
                        content_type="application/json")


# 店家展览图
def viewforseller(request):
    img = []
    queryset = Images.objects.all()
    for i in queryset:
        img.append({'img': i.url_0})
    return HttpResponse(json.dumps({"status": 1, "msg": "OK!", "data": img}, ensure_ascii=False),
                        content_type="application/json")


# 店家菜单预览
def viewtodo(request):
    data = []
    queryset = DiskTest.objects.all()
    for i in queryset:
        diskid = i.disk_id
        id=i.id
        imgs = Images.objects.filter(disk_id=diskid)
        for j in imgs:
            img = j.url_0
            break
        name = i.name
        price = i.price
        description = i.description;
        if i.is_single == 1:
            is_single = '是'
        else:
            is_single = '否'
        if i.support_takeaway == 1:
            support_takeaway = '是'
        else:
            support_takeaway = '否'
        data.append({'diskid':id,'img': img, 'name': name, 'price': price, 'is_single': is_single,
                     'description': description, 'support_takeaway': support_takeaway})
    return HttpResponse(json.dumps({"status": 1, "msg": "OK!", "data": data}, ensure_ascii=False),
                        content_type="application/json")


# 店家上菜
def addmenu(request):
    name = request.GET.get('name')
    description = request.GET.get('description')
    catagory_id = 67
    is_single = request.GET.get('is_single')
    if is_single == '是':
        is_single = True
    else:
        is_single = False
    support_takeaway = request.GET.get('support_takeaway')
    if support_takeaway == '是':
        support_takeaway = 1
    else:
        support_takeaway = 0
    price = request.GET.get('price')
    imgurl = request.GET.get('url')
    if len(name) == 0 or len(description) == 0 or len(imgurl) == 0:
        return HttpResponse(json.dumps({"status": 1, "msg": "有空数据!!", "data": ""}, ensure_ascii=False),
                            content_type="application/json")
    sort = 3
    queryset = DiskTest.objects.all()
    id = 2
    for i in queryset:
        id=max(id,i.id)
    id=id+1
    disk_id = id
    disk = DiskTest()
    disk.id = id
    disk.disk_id = disk_id
    disk.name = name
    disk.description = description
    disk.category_id = catagory_id
    disk.is_single = is_single
    disk.support_takeaway = support_takeaway
    disk.price = price
    disk.sort = sort
    disk.save()
    img = Images()
    queryset = Images.objects.all()
    id = 2
    for i in queryset:
        id = max(id, i.id)
    id = id + 1
    img.id=id
    img.disk_id = disk_id
    img.url_0 = imgurl
    img.url_1 = imgurl
    img.save()
    print(img)
    print('success ')
    return HttpResponse(json.dumps({"status": 1, "msg": "插入成功", "data": ""}, ensure_ascii=False),
                        content_type="application/json")


# 删除菜品
def deleteMenu(request):
    name = request.GET.get('diskname')
    print(name)
    disks = DiskTest.objects.filter(name=name)
    print(disks)
    for i in disks:
        img = Images.objects.filter(disk_id=i.disk_id)
        img.delete()
    disks.delete()
    return HttpResponse(json.dumps({"status": 1, "msg": "删除成功", "data": ""}, ensure_ascii=False),
                        content_type="application/json")


# 商家获取所有用户信息

# 用户信息设置
def usersinfo(request):
    users = UserInfo.objects.all()
    data = []
    for userinfo in users:
        p_temp = {
            'userid': userinfo.userId,
            "username": userinfo.username,
            "telphone": userinfo.telphone,
            "gender": userinfo.gender,
            "birthday": userinfo.birthday,
            "url": userinfo.url
        }
        data.append(p_temp)
    return HttpResponse(json.dumps({"status": 1, "msg": "OK!", "data": data}, ensure_ascii=False),
                        content_type="application/json")


# 根据用户id删除用户
def deluser(request):
    id = request.GET.get('deluser')
    usersinfo = UserInfo.objects.get(userId=id)
    users = UserTest.objects.filter(userId=id)
    for user in users:
        user.delete()
    usersinfo.delete()
    return HttpResponse(json.dumps({"status": 1, "msg": "删除成功", "data": ""}, ensure_ascii=False),
                        content_type="application/json")


# 店家改菜 根据用户id修改菜
def altermenu(request):
    name = request.GET.get('name')
    id=request.GET.get('id')
    description = request.GET.get('description')
    catagory_id = 67
    is_single = request.GET.get('is_single')
    if is_single == '是':
        is_single = True
    else:
        is_single = False
    support_takeaway = request.GET.get('support_takeaway')
    if support_takeaway == '是':
        support_takeaway = 1
    else:
        support_takeaway = 0
    price = request.GET.get('price')
    imgurl = request.GET.get('url')
    if len(name) == 0 or len(description) == 0 or len(imgurl) == 0:
        return HttpResponse(json.dumps({"status": 1, "msg": "有空数据!!", "data": ""}, ensure_ascii=False),
                            content_type="application/json")
    sort = 3
    queryset = DiskTest.objects.filter(id=id)
    for disk in queryset:
        disk.name = name
        disk.description = description
        disk.category_id = catagory_id
        disk.is_single = is_single
        disk.support_takeaway = support_takeaway
        disk.price = price
        disk.sort = sort
        disk.save()
        imgs = Images.objects.filter(disk_id=disk.disk_id)
        for img in imgs:
            img.url_0 = imgurl
            img.url_1 = imgurl
            img.save()
    return HttpResponse(json.dumps({"status": 1, "msg": "修改成功！！", "data": ""}, ensure_ascii=False),
                        content_type="application/json")


# 商家改变用户信息
def alteruser(request):
    id = request.GET.get('id')
    url = request.GET.get('url')
    telephone = request.GET.get('telephone')
    birthday = request.GET.get('birthday')
    username = request.GET.get('username')
    if len(url) == 0 or len(username) == 0 or len(birthday) == 0 or len(telephone) == 0:
        return HttpResponse(json.dumps({"status": 1, "msg": "用户信息修改失败！！", "data": ""}, ensure_ascii=False),
                            content_type="application/json")
    user = UserInfo.objects.get(userId=id)
    user.url = url
    user.birthday = birthday
    user.telphone = telephone
    user.username = username
    user.save()
    return HttpResponse(json.dumps({"status": 1, "msg": "改变用户信息成功！！", "data": ""}, ensure_ascii=False),
                        content_type="application/json")


# def orderall(request):找出所有订单
def orderall(request):
    data = []  # 需要找出所有订单    一份订单一个id，是一个字典，同时一份订单中的items也是一个字典
    # userName=request.GET.get("userName")
    userName = "Tang"  # 暂时用静态数据
    id = 1
    orderlist = OrderTest.objects.all()
    for m in orderlist:
        items = []
        for i in ItemTest.objects.filter(orderId=m.orderId):
            # 装菜品
            p_temp = {
                "quantity": i.quantity,
                "total_fee": '%.2f' % (i.total_fee),
                "price": i.price,
                "sname": i.sname,
                "image": i.image
            }
            items.append(p_temp)
        if m.state==0:
            message='待接单'
        elif m.state==1:
            message='待完成'
        else:
            message='已完成'
        p_temp_0 = {
            "id": id,  # 表示这是这个人的第几份订单
            "total_fee": '%.2f' % (m.total_fee),
            "payment": '%.2f' % (m.payment),
            "created_at": m.created_at,
            "remarks": m.remarks,
            "shopName": m.shopName,
            "items": items,
            "orderId": m.orderId,
            'state':m.state,
            'message':message
        }
        id = id + 1
        data.append(p_temp_0)
    return HttpResponse(json.dumps({"status": 200, "msg": "OK!", "data": data}, ensure_ascii=False),
                        content_type="application/json")
# def ordertobegin(request):待接单所有订单
def ordertobegin(request):
    data = []  # 需要找出所有订单    一份订单一个id，是一个字典，同时一份订单中的items也是一个字典
    # userName=request.GET.get("userName")
    # userName = "Tang"  # 暂时用静态数据
    id = 1
    orderlist = OrderTest.objects.filter(state=0)
    for m in orderlist:
        items = []
        for i in ItemTest.objects.filter(orderId=m.orderId):
            # 装菜品
            p_temp = {
                "quantity": i.quantity,
                "total_fee": '%.2f' % (i.total_fee),
                "price": i.price,
                "sname": i.sname,
                "image": i.image
            }
            items.append(p_temp)

        p_temp_0 = {
            "id": id,  # 表示这是这个人的第几份订单
            "total_fee": '%.2f' % (m.total_fee),
            "payment": '%.2f' % (m.payment),
            "created_at": m.created_at,
            "remarks": m.remarks,
            "shopName": m.shopName,
            "items": items,
            "orderId": m.orderId,
            'state':m.state,
            'allid':m.id
        }
        id = id + 1
        data.append(p_temp_0)
    return HttpResponse(json.dumps({"status": 200, "msg": "OK!", "data": data}, ensure_ascii=False),
                        content_type="application/json")
#开始接单
def beginoder(request):
    orderId = request.GET.get("id")
    order_begin = OrderTest.objects.get(id=orderId)
    order_begin.state=1
    order_begin.save()
    return HttpResponse(json.dumps({"status": 200, "msg": "OK!", "data": ""}, ensure_ascii=False),
                        content_type="application/json")
# def ordertofinish(request):待完成所有订单
def ordertofinish(request):
    data = []  # 需要找出所有订单    一份订单一个id，是一个字典，同时一份订单中的items也是一个字典
    # userName=request.GET.get("userName")
    # userName = "Tang"  # 暂时用静态数据
    id = 1
    orderlist = OrderTest.objects.filter(state=1)
    for m in orderlist:
        items = []
        for i in ItemTest.objects.filter(orderId=m.orderId):
            # 装菜品
            p_temp = {
                "quantity": i.quantity,
                "total_fee": '%.2f' % (i.total_fee),
                "price": i.price,
                "sname": i.sname,
                "image": i.image
            }
            items.append(p_temp)

        p_temp_0 = {
            "id": id,  # 表示这是这个人的第几份订单
            "total_fee": '%.2f' % (m.total_fee),
            "payment": '%.2f' % (m.payment),
            "created_at": m.created_at,
            "remarks": m.remarks,
            "shopName": m.shopName,
            "items": items,
            "orderId": m.orderId,
            'state':m.state,
            'allid':m.id
        }
        id = id + 1
        data.append(p_temp_0)
    return HttpResponse(json.dumps({"status": 200, "msg": "OK!", "data": data}, ensure_ascii=False),
                        content_type="application/json")

#完成接单
def finishoder(request):
    orderId = request.GET.get("id")
    order_begin = OrderTest.objects.get(id=orderId)
    order_begin.state = 2
    order_begin.save()
    return HttpResponse(json.dumps({"status": 200, "msg": "OK!", "data": ""}, ensure_ascii=False),
                        content_type="application/json")