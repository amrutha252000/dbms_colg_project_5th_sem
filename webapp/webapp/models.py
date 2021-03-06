from django.db import models
#from PIL import Image
#from imagekit.models import ImageSpecField
#from imagekit.processors import ResizeToFill
from django.utils import timezone
from datetime import date
import datetime
from datetime import datetime
# Create your models here.

class product(models.Model):
    sid = models.ForeignKey('seller', on_delete=models.CASCADE,null=False)
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='product_image', blank=True)
    price = models.IntegerField(blank=True, default=0)
       

    class Meta:
        db_table = "product"

    def getabsoluteurl(self):
	    return "/product/%i/" % self.id    

    def __str__(self):
	    return self.title 

class seller(models.Model):
    s_email = models.ForeignKey('buyer', on_delete=models.CASCADE)
    s_name = models.CharField(max_length=50)
    s_address = models.CharField(max_length=200)
    s_phno = models.CharField(max_length=20)

	# def __str__(self):
    #     return self.s_name
    
    class Meta:
        db_table = "seller"

class buyer(models.Model):
    b_email = models.CharField(max_length=100, primary_key=True)
    b_name = models.CharField(max_length=100)
    b_phno = models.CharField(max_length=10, null=True)

    class Meta:
        db_table = "buyer"

class cart(models.Model):
    bid = models.ForeignKey('buyer', on_delete=models.CASCADE, null=False)
    pid = models.ForeignKey('product',	on_delete=models.CASCADE)
    sid = models.ForeignKey('seller', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        unique_together = (("pid", "bid"),)
        db_table = "cart"


class orders(models.Model):
    # oid = models.CharField(editable=False, max_length=128)
    bid = models.ForeignKey('buyer', on_delete=models.CASCADE)
    pid = models.ForeignKey('product', on_delete=models.CASCADE)
    sid = models.ForeignKey('seller', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.today())
    price = models.IntegerField()
    # quantity = models.IntegerField()
    address = models.ForeignKey('address', on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('bid', 'pid', 'sid','created_at')
        db_table = "orders"


class address(models.Model):
    bid = models.ForeignKey('buyer', on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=30)
    phno = models.CharField(max_length=10)
    address = models.TextField()
    
    class Meta:
        db_table = "address"