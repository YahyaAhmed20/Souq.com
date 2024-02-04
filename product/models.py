from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    # name default value
    PRDname = models.CharField(max_length=255,verbose_name=(("Product Name")) )
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
    PRDIimage = models.ImageField(upload_to='photos/%y/%m/%d', default='path/to/default/image.jpg')

    def __str__(self):
        if self.PRDIproduct and hasattr(self.PRDIproduct, 'name') and self.PRDIproduct.name:
            return f"{self.PRDIproduct.name} - Image"
        else:
            return "Unassociated Image"
#   f"{self.product.name} - Image"

    