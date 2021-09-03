from django.db import models

# Create your models here.
class Images(models.Model):
    disk_id=models.IntegerField('disk_id', default=0)
    url_0=models.CharField('url_0', max_length=100)
    url_1=models.CharField('url_1', max_length=100)

class DiskTest(models.Model):
    disk_id=models.IntegerField('disk_id', default=0)
    name=models.CharField('name', max_length=100)
    description=models.CharField('description', max_length=100)
    category_id=models.IntegerField('category_id', default=0)
    is_single=models.BooleanField('is_single',default=False)
    support_takeaway=models.IntegerField('support_takeaway', default=0)
    price=models.CharField('price', max_length=100)
    sort=models.IntegerField('sort',default=0)

class MenuTest(models.Model):
    menuId=models.IntegerField('menuId', default=0)
    name=models.CharField('name', max_length=100)
    sort = models.IntegerField('sort', default=0)

class ItemTest(models.Model):
    openId=models.CharField('openId', max_length=100,default="")
    orderId = models.CharField('orderId', max_length=100)
    sname=models.CharField('sname', max_length=100)
    quantity= models.IntegerField('quantity', default=0)
    price=models.CharField('price', max_length=100)   #与disktest里面的同类型
    image=models.CharField('image', max_length=100)
    total_fee= models.IntegerField('quantity', default=0)
class OrderTest(models.Model):
    total_fee= models.IntegerField('quantity', default=0)
    remarks=models.CharField('remarks', max_length=100)
    payment= models.IntegerField('quantity', default=0)
    shopName=models.CharField('shopName', max_length=100)
    orderId = models.CharField('orderId', max_length=100)   #根据时间生成的，因为没有日月，仍可能重复
    created_at=models.CharField('created_at', max_length=100)
    userName=models.CharField('userName', max_length=100)    #备用  用于找到是哪个人的订单
    openId=models.CharField('openId', max_length=100)           #备用  后面可能用到
    state = models.IntegerField('state', default=0)
class AddressItemTest(models.Model):
    user_id=models.CharField('user_id', max_length=100)
    name=models.CharField('name', max_length=100)
    phone=models.CharField('phone', max_length=100)
    gender=models.IntegerField('is_default', default=0)
    address=models.CharField('address', max_length=100)
    complete_address=models.CharField('complete_address', max_length=100)
    description=models.CharField('description', max_length=100)
    latitude=models.CharField('latitude', max_length=100)
    longitude=models.CharField('longitude', max_length=100)
    is_default= models.IntegerField('is_default', default=0)

class UserTest(models.Model):
    userId=models.CharField('userId', max_length=100)
    password=models.CharField('password', max_length=100)
    userName=models.CharField('userName', max_length=100)

class UserInfo(models.Model):
    userId=models.CharField('userId', max_length=100)
    username=models.CharField('userName', max_length=100)
    telphone=models.CharField('telphone', max_length=100)
    gender=models.IntegerField('is_default', default=0)
    birthday = models.CharField('birthday', max_length=100)
    url=models.CharField('url', max_length=100)