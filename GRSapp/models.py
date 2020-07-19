from django.db import models
import random


class ContactModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)
    def __str__(self):
        return self.name+','+self.email
    

class UsersModal(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    gender = models.CharField(max_length=7)
    user_pic = models.ImageField(upload_to="user_pics/",default="ImageNotFound")
    dob = models.DateField()
    password = models.CharField(max_length=40)

    def __str__(self):
        return self.firstname

class itemslist(models.Model):
    itemname = models.CharField(max_length=50)
    itemdesc = models.TextField(max_length=100)
    itempic  = models.ImageField(upload_to="itemspics",default="Image Not Found")

    def __str__(self):
        return self.itemname
    

class Mobiles(models.Model):
    brandname = models.CharField(max_length=50)
    modelname = models.CharField(max_length=50)
    battery_cap = models.IntegerField()
    internal_mem = models.IntegerField()
    front_cam = models.IntegerField()
    back_cam = models.IntegerField()
    display = models.IntegerField()
    ram = models.IntegerField()
    mob_pic = models.ImageField(upload_to="Mobiles",default="Image Not Found")
    price = models.IntegerField()
    rating = models.IntegerField(default=0)
    hearts = models.IntegerField(default=random.randint(18,25))

    class Meta:
        ordering = ['-id']
    
    def __str__(self):
        return self.brandname+" , "+self.modelname

class Laptops(models.Model):
    brandname = models.CharField(max_length=50)
    modelname = models.CharField(max_length=50)
    battery_cap = models.IntegerField()
    internal_mem = models.CharField(max_length=20)
    ram = models.IntegerField()
    price = models.IntegerField()
    rating = models.IntegerField(default=0)
    hearts = models.IntegerField(default=0)
    display = models.CharField(max_length=25)
    graphics = models.CharField(max_length=30)
    lap_pic = models.ImageField(upload_to="Laptops",default="Image Not Found")
    class Meta:
        ordering = ['-id']
    def __str__(self):
        return self.brandname+','+self.modelname


class HeadSet(models.Model):
    brandname = models.CharField(max_length=50)
    modelname = models.CharField(max_length=50)
    price = models.IntegerField()
    is_wireless = models.BooleanField()
    is_microphone_avbl = models.BooleanField()
    built_matrl = models.CharField(max_length=60)
    spec = models.TextField()
    hset_pic = models.ImageField(upload_to="HeadSet",default="Image Not Found")
    rating = models.IntegerField(default=random.randint(1,6))
    hearts = models.IntegerField(default=random.randint(10,35))
    class Meta:
        ordering = ['-id']
    def __str__(self):
        return self.brandname+','+self.modelname

class Camera(models.Model):
    brandname = models.CharField(max_length=50)
    modelname = models.CharField(max_length=50)
    price = models.IntegerField()
    cam_pic = models.ImageField(upload_to="Cameras",default="Image Not Found")
    megapixel = models.IntegerField()
    is_raw_mode = models.BooleanField()
    battery_cap = models.IntegerField()
    is_autofocus = models.BooleanField()
    is_image_stable = models.BooleanField()
    rating = models.IntegerField(default=random.randint(1,6))
    hearts = models.IntegerField(default=random.randint(10,35))
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.brandname+','+self.modelname


class Powerbank(models.Model):
    brandname = models.CharField(max_length=50)
    modelname = models.CharField(max_length=50)
    price = models.IntegerField()
    pbank_pic = models.ImageField(upload_to="Powerbank",default="Image Not Found")
    battery_cap = models.IntegerField(default=0)
    no_outputs = models.IntegerField()
    is_C_port = models.BooleanField()
    is_USB_port = models.BooleanField()
    is_B_port = models.BooleanField()
    rating = models.IntegerField(default=random.randint(1,6))
    hearts = models.IntegerField(default=random.randint(10,35))
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.brandname + ',' + self.modelname  

class Refrigerator(models.Model):
    brandname = models.CharField(max_length=50)
    modelname = models.CharField(max_length=50)
    price = models.IntegerField()
    colour = models.CharField(max_length=50)
    refrig_pic = models.ImageField(upload_to="Refrigerator",default="Image Not Found")
    Capacity = models.IntegerField()
    Warranty = models.IntegerField()
    double_door = models.BooleanField()
    single_door = models.BooleanField()
    rating = models.IntegerField(default=random.randint(1,6))
    hearts = models.IntegerField(default=random.randint(10,35))
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.brandname + ',' + self.modelname  

class Kettle(models.Model):
    brandname = models.CharField(max_length=50)
    modelname = models.CharField(max_length=50)
    price = models.IntegerField()
    kettle_pic = models.ImageField(upload_to="Kettle",default="Image Not Found")
    colour = models.CharField(max_length=15)
    max_temp = models.IntegerField()
    is_auto_manage = models.BooleanField()
    spec = models.TextField(max_length=1000)
    body_matrl = models.CharField(max_length=50)
    optr_volt = models.IntegerField()
    rating = models.IntegerField(default=random.randint(1,6))
    hearts = models.IntegerField(default=random.randint(10,35))
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.brandname + ',' + self.modelname

class Television(models.Model):
    brandname = models.CharField(max_length=50)
    modelname = models.CharField(max_length=50)
    price = models.IntegerField()
    tv_pic = models.ImageField(upload_to="Television",default="Image Not Found")
    color = models.CharField(max_length=20)
    disp_len = models.IntegerField()
    spec = models.TextField()
    is_smart_tv = models.BooleanField()
    rating = models.IntegerField(default=random.randint(1,6))
    hearts = models.IntegerField(default=random.randint(10,35))
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.brandname + ',' + self.modelname


class WashingMachine(models.Model):
    brandname = models.CharField(max_length=50)
    modelname = models.CharField(max_length=50)
    price = models.IntegerField()
    wm_pic = models.ImageField(upload_to="WashingMachine",default="Image Not Found")
    ltr_cap = models.IntegerField()
    direction = (
        ('vertical','Vertical'),
        ('horizontal','Horizontal')
    )
    drum_dir = models.CharField(max_length=10,choices=direction)
    is_smart_wm = models.BooleanField()
    is_auto_dry = models.BooleanField()
    colour = models.CharField(max_length=15)
    optr_volt = models.IntegerField()
    rating = models.IntegerField(default=random.randint(1,6))
    hearts = models.IntegerField(default=random.randint(10,35))
    class Meta:
        ordering = ['-id']


    def __str__(self):
        return self.brandname + ',' + self.modelname

# all review models goes here

class mobilereview(models.Model):
    userid = models.CharField(max_length=50)
    mobileid = models.IntegerField()
    reviewmsg = models.TextField()
    class Meta:
        ordering = ['-id']
    def __str__(self):
        return self.reviewmsg

class laptopreview(models.Model):
    userid = models.CharField(max_length=50)
    laptopid = models.IntegerField()
    reviewmsg = models.TextField()
    class Meta:
        ordering = ['-id']
    def __str__(self):
        return self.reviewmsg

class headsetreview(models.Model):
    userid = models.CharField(max_length=50)
    headsetid = models.IntegerField()
    reviewmsg = models.TextField()
    class Meta:
        ordering = ['-id']
    def __str__(self):
        return self.reviewmsg

class camerareview(models.Model):
    userid = models.CharField(max_length=50)
    cameraid = models.IntegerField()
    reviewmsg = models.TextField()
    class Meta:
        ordering = ['-id']
    def __str__(self):
        return self.reviewmsg

class powerbankreview(models.Model):
    userid = models.CharField(max_length=50)
    powerbankid = models.IntegerField()
    reviewmsg = models.TextField()
    class Meta:
        ordering = ['-id']
    def __str__(self):
        return self.reviewmsg

    
class kettlereview(models.Model):
    userid = models.CharField(max_length=50)
    kettleid = models.IntegerField()
    reviewmsg = models.TextField()
    class Meta:
        ordering = ['-id']
    def __str__(self):
        return self.reviewmsg

class washmanchinereview(models.Model):
    userid = models.CharField(max_length=50)
    washmachineid = models.IntegerField()
    reviewmsg = models.TextField()
    class Meta:
        ordering = ['-id']
    def __str__(self):
        return self.reviewmsg

class fridgereview(models.Model):
    userid = models.CharField(max_length=50)
    fridgeid = models.IntegerField()
    reviewmsg = models.TextField()
    class Meta:
        ordering = ['-id']
    def __str__(self):
        return self.reviewmsg
    
class televisionreview(models.Model):
    userid = models.CharField(max_length=50)
    televisionid = models.IntegerField()
    reviewmsg = models.TextField()
    class Meta:
        ordering = ['-id']
    def __str__(self):
        return self.reviewmsg




    







