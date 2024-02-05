from django.db import models

# Create your models here.

# class brand
class Brand(models.Model):
#inside class brand
    BRDName = models.CharField(max_length=255,verbose_name=(("Brand Name")) )
    #more optio
    BRDDescription = models.TextField(max_length=50,verbose_name=("Brand Description"))
    
    def __str__(self):
        return self.BRDName
    
class Variant(models.Model):
    NRTName = models.CharField(max_length=255,verbose_name=(("Variant Name")) )
    #more optio
    VRTDescription = models.TextField(max_length=50,verbose_name=("Variant Description"))
    
    
    def __str__(self) :
        return self.NRTName