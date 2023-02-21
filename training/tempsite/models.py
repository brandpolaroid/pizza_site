from django.db import models


class Pizza(models.Model):
    text = models.TextField()
    price = models.IntegerField(default=0)
    picture = models.ImageField(upload_to="uploads/")
    name = models.CharField(max_length=50, default="")


class Order(models.Model):
    price = models.IntegerField(default=0)
    user_ip = models.CharField(default=None, max_length=50)
    product_id = models.JSONField(default=None)


class Offered(models.Model):
    user_phone = models.CharField(default=None, max_length=50)
    user_id = models.IntegerField(default=0)
    user_address = models.CharField(default=None, max_length=300)
    user_name = models.CharField(default=None, max_length=20)
    product_id = models.JSONField(default=None)
    order_price = models.IntegerField(default=0)
    date_time_start = models.DateTimeField()
    date_time_stop = models.DateTimeField(null=True)
    status = models.IntegerField(default=0)

















# class Person(models.Model):
#     name = models.CharField(max_length=20, default='None')
#     age = models.IntegerField(default=0)
#     cash = models.IntegerField(default=0)
#
#
# class Customer(models.Model):
#     name = models.CharField(max_length=20, default='None')
#     age = models.IntegerField(default=0)
#     password = models.CharField(max_length=20, default='None')
#     email = models.CharField(max_length=50, default='None')


# class Messages(models.Model):
#     text = models.TextField()
#     owner = models.CharField(max_length=20, default="")
#     to = models.CharField(max_length=20, default="")