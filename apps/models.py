from django.db import models

class Productcategory(models.Model):
      category_name=models.CharField(max_length=100)
      img=models.ImageField(upload_to='categoryImg')

def __str__(self):
        return self.Productcategory
  

class Products(models.Model):
      product_name=models.CharField(max_length=100)
      categoris=models.ForeignKey(Productcategory, verbose_name='product Category',on_delete=models.CASCADE)
      image=models.ImageField(upload_to='productImg')
      hover_image=models.ImageField(upload_to='productImg',blank=True,null=True)
      price=models.IntegerField
      discount_price=models.IntegerField(blank=True,null=True)
      product_purchase_price = models.IntegerField(blank=True,null=True)
      sort_description=models.CharField(max_length=100,blank=True,null=True)
      description=models.CharField(max_length=300)
      additional_description=models.CharField(max_length=300,blank=True,null=True)
      stock_quentity=models.PositiveIntegerField()
class Meta:
    verbose_name ="products"

    def __str__(self):
        pass

# Create your models here.
