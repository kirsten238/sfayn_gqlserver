from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProductCategory(models.Model):
    LEVEL_CHOICES = (
        (1,	"Level 1"),
        (2,	"Level 2"),
        (3,	"Level 3"),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    level = models.IntegerField(null=True, choices=LEVEL_CHOICES) 

    def __str__(self):
        return "Level({}) ParentId({}) Id({}) Name({})".format(self.level, self.parent_id, self.id, self.name, self.level)


class ProductParent(models.Model):
    STATUS_CHOICES = (
        (0,	"Active"),
    )
    #we can add more attributes later
    id = models.AutoField(primary_key=True)
    parent_sn = models.CharField(max_length=50) #CharField to accept multiple sku datatype 
    title = models.CharField(max_length=100, null=True) 
    category = models.ForeignKey("product.ProductCategory", on_delete=models.CASCADE, null=True, related_name="cat2product") 
    goods_brand = models.CharField(max_length=30, null=True, blank=True)
    goods_desc = models.TextField(null=True) 
    status = models.IntegerField(null=True, choices=STATUS_CHOICES) 
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user2product")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return "ParentSn:{} Title:{}".format(self.parent_sn, self.title)


class ProductVariant(models.Model):
    id = models.AutoField(primary_key=True)
    parent_sn = models.ForeignKey("product.ProductParent", on_delete=models.CASCADE, null=True, related_name="product2variants") 
    sku = models.CharField(max_length=50)
    quantity = models.IntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True) #Colour
    options = models.CharField(max_length=50, null=True, blank=True) # Red/Blue?
    img_url = models.CharField(max_length=250, null=True, blank=True) #TODO imagefield
    default = models.BooleanField(default=False)

    def __str__(self):
        return "{}-{}-{}-{}".format(self.parent_sn_id, self.sku, self.name, self.options)



class ProductImage(models.Model):
    id = models.AutoField(primary_key=True)
    parent_sn = models.ForeignKey("product.ProductParent", on_delete=models.CASCADE, null=True, related_name="parent2image") 
    img_url = models.CharField(max_length=250, null=True) #TODO imagefield
    cover_photo = models.BooleanField(default=False)


class ProductVideo(models.Model):
    id = models.AutoField(primary_key=True)
    parent_sn = models.ForeignKey("product.ProductParent", on_delete=models.CASCADE, null=True, related_name="parent2video") 
    video_url = models.CharField(max_length=250, null=True) #TODO filefield?