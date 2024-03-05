from django.db import models

# Create your models here.

class Productcategery(models.Model):
    Product_categery_id=models.IntegerField(primary_key=True)
    Product_categery_name=models.CharField(max_length=100)

    def __str__(self):
        return self.Product_categery_name



class Product(models.Model):
    Product_categery_id=models.ForeignKey(Productcategery,on_delete=models.CASCADE)
    Product_id=models.IntegerField()
    Product_name=models.CharField(max_length=100)
    Product_price=models.IntegerField()
    Product_brand=models.CharField(max_length=100)


    def __str__(self):
        return self.Product_name


