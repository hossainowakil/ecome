from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=120)
    age = models.IntegerField()
    address = models.TextField(max_length=90)
    is_activ = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return  f"{self.name} | {self.age}"
    

class Catagory(models.Model):
    name = models.CharField(max_length=200)
    description =models.TextField(max_length=250)  


    def __str__(self):
        return  f"{self.name} | {self.description}"

class product(models.Model):
    catagory= models.ForeignKey(Catagory,on_delete=models.CASCADE)
    name = models.CharField(max_length=56)
    image=models.ImageField(upload_to='image/product' ,blank=True, null=True)
    price = models.IntegerField()

    def __str__(self):
        return  f"{self.name} | {self.price}"

    
