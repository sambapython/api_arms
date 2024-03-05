from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser



class Assignment(models.Model):
    name = models.CharField(max_length=250)    
    address = models.CharField(max_length=250)    
    email = models.CharField(max_length=250)    
    floor = models.CharField(max_length=250)    
    resources = models.CharField(max_length=250)    
class BaseAbstarctModel(models.Model):
     name = models.CharField(max_length=250, unique=True)
     class Meta:
         abstract = True

class Role(BaseAbstarctModel):
    pass
    #name = models.CharField(max_length=100, unique=True)

class MyUser(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        #role_inst = Role.objects.get(id=kwargs.get("role_id"))

# Create your models here.
def validate_email(value):
    if value.isdigit():
        raise ValidationError("expecting alphanueric values")
class Category(models.Model):
    name = models.CharField(max_length=250)    

class SalesOrder(models.Model):
    description = models.TextField(max_length=250)

class PurchaseOrder(models.Model):
    description = models.TextField(max_length=250)
class Product(models.Model):
    name = models.CharField(max_length=250)
    product_unque_number = models.CharField(max_length=250, unique=True)  
    category = models.ForeignKey(Category, on_delete=models.PROTECT) 
    purchase_orders = models.ManyToManyField(PurchaseOrder)
    sales_orders = models.ManyToManyField(SalesOrder)

class ProductCost(models.Model):
    prodcut = models.ForeignKey(Product, on_delete=models.PROTECT)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
class OpeningStock(models.Model):
    prodcut = models.ForeignKey(Product, on_delete=models.PROTECT)
    stock = models.DecimalField(max_digits=10, decimal_places=2)
"""
productpurachaseorder
id
product_id
purchaseorder_id

productsalesoredder
id
product_id
salesorder_id
"""
#stock on hand




class Person(BaseAbstarctModel):
    #name = models.CharField(max_length=250, unique=True)
    email = models.EmailField(max_length=250, default="", validators=(validate_email,))
    age = models.IntegerField(default=0)
    created_by = models.ForeignKey(MyUser, on_delete=models.PROTECT, null=True)
    """
    Person.objects.filter(email="")
    Person.objects.filter(created_by=id_user)
    Person.objects.filter(created_by__username="username")
    "sambapython@gmaill.com"
    "SambApyThon@gmaill.com".lower()

    Person.objects.filter(created_by__username__lower="username")
    Person.objects.filter(first_name__startswith="jay") and istances of filtered records
    
    """

class Region(BaseAbstarctModel):
    pass
    #name = models.CharField(max_length=250, unique=True)

class Country(BaseAbstarctModel):
    #name = models.CharField(max_length=250, unique=True)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)

class State(BaseAbstarctModel):
    #name = models.CharField(max_length=250, unique=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
class Address(models.Model):
    city = models.CharField(max_length=250)
    street = models.CharField(max_length=250)
    pincode = models.CharField(max_length=50)



class Api(BaseAbstarctModel):
    pass
    #name = models.CharField(max_length=250, unique=True)

class Permissions(models.Model):
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    api = models.ForeignKey(Api, on_delete=models.PROTECT)
    has_get = models.BooleanField(default=False)
    has_post = models.BooleanField(default=False)
    has_put = models.BooleanField(default=False)
    has_delete = models.BooleanField(default=False)

#onetoone
"""
samba: userrole
UserPRofile: 

UserProfile.get(userid=reqest.user.id).role.id
"""
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.PROTECT)
#     role = models.ForeignKey(Role, on_delete=models.PROTECT)

#from django.contrib.auth.models import User.
# dont use User model use the model app1.models.MyUser
#class MyUser()
# what is abstract models?

"""
Normal
abstarct models
inherited models
proxy models
"""
"""
User
UserProfile model

class UserProfile(models.model):
    user =  models.OneToOne()


class UserProfile(User):
    pancard = models.CharField(max_length=100)


class UserProxyModel(User):
    # we will not add any extra columns.
    # procy model will not allow to add columns
    # we can add operations. these operations act on parent mode.
    # There is no table created for this.
    class Meta:
        __proxy__=True


"""

        



    

