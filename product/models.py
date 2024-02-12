from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    # name default value
    PRDname = models.CharField(max_length=255,verbose_name=_(("Product Name")) )
    PRDCategory = models.ForeignKey('Category',on_delete=models.CASCADE,null=True, blank=True,verbose_name=_(("Product Category")))
    
    PRDBrand = models.ForeignKey('settings.Brand', on_delete=models.CASCADE ,null=True, blank=True,verbose_name=_(("Product Brand")))
    PRDdescription = models.TextField(max_length=500,verbose_name=_("Product Description"))
    PRDimage = models.ImageField(upload_to='product/',blank=True,null=True)

    PRDprice = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Price"))
    PRDdiscount=models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Discount Price"))
    PRDcost = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Cost"))
    PRDactive=models.BooleanField(default=True,verbose_name=_(("Active")))
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now)
    PRDSlug=models.SlugField(blank=True,null=True ,verbose_name=_(("Slug")))
    PRDisNew=models.BooleanField(default=True ,verbose_name=_(("New Product")))
    PRDisBestSeller=models.BooleanField(default=False ,verbose_name=_(("Best Seller Product")))
    


    def save(self, *args, **kwargs):
            self.PRDSlug = slugify(self.PRDname)
            super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("products:product_details", kwargs={'slug': self.PRDSlug})
    
    
    
    # return name
    def __str__(self):
        return self.PRDname
    #     PRDimage = models.ImageField(upload_to='photos/%y/%m/%d', default='path/to/default/image.jpg')

    

class ProductImage(models.Model):
    PRDIproduct = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name=_((" product ")))
    PRDIimage = models.ImageField(upload_to='product/',blank=True,null=True)

    def __str__(self):
        return str(self.PRDIproduct)
#   f"{self.product.name} - Image"

# class category
class Category(models.Model):
    CATName=models.CharField(max_length=255,verbose_name=_(("Category Name")))
    CATParent=models.ForeignKey('self' ,limit_choices_to={'CATParent__isnull':True},on_delete=models.CASCADE, blank=True, null=True,verbose_name=_(("Category")))
    CATdescription = models.TextField(max_length=50, default='', verbose_name=_("Category Description"))
    CATImg=models.ImageField(upload_to='Category/%y/%m/%d',verbose_name=_(("Category Image ")))
    
    
    def __str__(self):
        return self.CATName
    
class ProductAlternatives(models.Model):
    PALTproduct=models.ForeignKey(Product, on_delete=models.CASCADE ,related_name="Main_products",verbose_name=_(("Product Name")))
    #PALTAlternatives
    PALTalternative=models.ManyToManyField(Product ,related_name="Alternative_Product",verbose_name=_(("Alternative Product")))
    
    def __str__(self) :
        return str(self.PALTproduct)
class ProductAccessories(models.Model):
     PACCproduct=models.ForeignKey(Product, on_delete=models.CASCADE ,related_name="Main_Accessories",verbose_name=_(("Accessory Name")))
    #PALTAlternatives
     PACCalternative=models.ManyToManyField(Product ,related_name="Accessories_Product",verbose_name=_(("Alternative Product")))
     
     def __str__(self):
         return str(self.PACCproduct)