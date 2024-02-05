from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    # name default value
    PRDname = models.CharField(max_length=255,verbose_name=(("Product Name")) )
    #category
    PRDCategory = models.ForeignKey('Category',on_delete=models.CASCADE,null=True, blank=True,verbose_name=(("Product Category")))
    #PRDBRAND
    PRDBrand = models.ForeignKey('settings.Brand', on_delete=models.CASCADE ,null=True, blank=True,verbose_name=(("Product Brand")))
    # description default value
    PRDdescription = models.TextField(max_length=50,verbose_name=("Product Description"))
    # price
    PRDprice = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=("Price"))
    # cost
    PRDcost = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=("Cost"))
    #created

    PRDactive=models.BooleanField(default=True,verbose_name=(("Active")))
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now)

    # return name
    def __str__(self):
        return self.PRDname
    #     PRDimage = models.ImageField(upload_to='photos/%y/%m/%d', default='path/to/default/image.jpg')

    

class ProductImage(models.Model):
    PRDIproduct = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name=((" product ")))
    PRDIimage = models.ImageField(upload_to='photos/%y/%m/%d', default='path/to/default/image.jpg',verbose_name=(("Product Image")))

    def __str__(self):
        return str(self.PRDIproduct)
#   f"{self.product.name} - Image"

# class category
class Category(models.Model):
    CATName=models.CharField(max_length=255,verbose_name=(("Category Name")))
    CATParent=models.ForeignKey('self' ,limit_choices_to={'CATParent__isnull':True},on_delete=models.CASCADE, blank=True, null=True,verbose_name=(("Category")))
    CATdescription = models.TextField(max_length=50, default='', verbose_name=("Category Description"))
    CATImg=models.ImageField(upload_to='Category/%y/%m/%d', default='path/to/default/image.jpg',verbose_name=(("Category Image ")))
    
    
    def __str__(self):
        return self.CATName
    
class ProductAlternatives(models.Model):
    PALTproduct=models.ForeignKey(Product, on_delete=models.CASCADE ,related_name="Main_products",verbose_name=(("Product Name")))
    #PALTAlternatives
    PALTalternative=models.ManyToManyField(Product ,related_name="Alternative_Product",verbose_name=(("Alternative Product")))
    
    def __str__(self) :
        return str(self.PALTproduct)
class ProductAccessories(models.Model):
     PACCproduct=models.ForeignKey(Product, on_delete=models.CASCADE ,related_name="Main_Accessories",verbose_name=(("Accessory Name")))
    #PALTAlternatives
     PACCalternative=models.ManyToManyField(Product ,related_name="Accessories_Product",verbose_name=(("Alternative Product")))
     
     def __str__(self):
         return str(self.PACCproduct)