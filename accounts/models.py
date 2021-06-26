from django.db import models


# Create your models here.



class flats(models.Model):
    city = models.ForeignKey('city' , on_delete=models.CASCADE)  
    address = models.TextField()
    img = models.ImageField(upload_to='pics',blank=True, null=True)
    img1 = models.ImageField(upload_to='pics',blank=True, null=True)
    img2 = models.ImageField(upload_to='pics',blank=True, null=True)
    img3 = models.ImageField(upload_to='pics',blank=True, null=True)
    sqr_ft = models.IntegerField()
    bhk = models.IntegerField()
    est_year = models.IntegerField()   
    rate = models.CharField(max_length=20)
    rent = models.BooleanField(default=False)
    sell = models.BooleanField(default=False)
    owner_fullname = models.CharField(max_length=50)
    owner_email = models.EmailField(max_length=250)
    owner_contact = models.CharField(max_length=10)
    def __str__(self):
        return self.owner_fullname    


class city(models.Model):
    location = models.CharField(max_length=50)
    img = models.ImageField(upload_to='pics')
  
    def __str__(self):
        return self.location

class contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile = models.CharField(max_length=10)
    message = models.TextField()

class contact_us(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile = models.CharField(max_length=10)
    message = models.TextField()
    def __str__(self):
        return self.first_name


class enquiry(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile = models.CharField(max_length=10)
   
    flats_id = models.IntegerField(default=1)
    message = models.TextField(default='')
    def __str__(self):
        return self.name

class enquiry_us(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile = models.CharField(max_length=10)
   
    flats_id = models.IntegerField(default=1)
    message = models.TextField(default='')
    def __str__(self):
        return self.name






    



