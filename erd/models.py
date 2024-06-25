from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from datetime import datetime
from django.contrib.auth.models import User
import os 
from django.utils.deconstruct import deconstructible
from django.db.models.signals import pre_save
from django.dispatch import receiver

@deconstructible
class GenerateProfileImagePath(object):
    def __init__(self):
        pass
    def __call__(self,instance,filename):
        ext=filename.split('.')[-1]
        path =f'media/accounts/{instance.user.id}/images/'
        name=f'profile_image.{ext}'
        return os.path.join(path,name)
    
user_profile_image_path=GenerateProfileImagePath()


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.FileField(upload_to=user_profile_image_path,blank=True,null=True)
    def __str__(self):
        return f'{self.user.username}\'s Profile'



# class Login(models.Model):
#     Userhandel=models.CharField(primary_key=True,max_length=100,blank=False)
#     Password=models.CharField(max_length=100,blank=False)
#     def __str__(self):
#         return self.Userhandel
#     class Meta:
#         ordering=['Userhandel']

    
class Register(models.Model):
    name=models.CharField(max_length=100,blank=False)
    emaill=models.CharField(primary_key=True,null=False,blank=False,max_length=100)
    Password=models.CharField(max_length=100,blank=False)
    RePassword=models.CharField(max_length=100,blank=False)
    PhoneNumber=models.CharField(null=False,blank=False,max_length=14)
    def __str__(self):
        return self.name
    class Meta:
        ordering=['name']




class Escort(models.Model):
    FirstName=models.CharField(max_length=100,null=False,blank=False)
    LasttName=models.CharField(max_length=100,null=False,blank=False)
    EscortID=models.AutoField(primary_key=True,null=False,blank=False)
    Email=models.CharField(max_length=100,blank=False)
    Password=models.CharField(max_length=100,blank=False)
    PhoneNumber=models.CharField(null=False,blank=False,max_length=14)
    yourHandel=models.CharField(max_length=100,blank=False)
    ProfilePicture=models.ImageField(upload_to='photos%y%m%d')
    Male=models.BooleanField(default=True)
    Female=models.BooleanField(default=False)
    LastModified=models.DateTimeField(auto_now=True,null=False,blank=False)

    def __str__(self):
        return self.yourHandel
    class Meta:
        ordering=['yourHandel']

class Diseases(models.Model):
    DiseasesID = models.AutoField(primary_key=True,null=False, blank=True)    
    Deasesname=models.CharField(max_length=100)
    DeasesDiscription=models.CharField(max_length=100)
    commen_symptoms=models.CharField(max_length=100)
    def __str__(self):
        return self.Deasesname
    class Meta:
        ordering=['Deasesname']        




class patient(models.Model):
    FirstName = models.CharField(max_length=100, null=False, blank=False)
    LasttName = models.CharField(max_length=100, null=False, blank=False)
    patientID = models.AutoField(primary_key=True, null=False, blank=False)
    EscortID = models.ForeignKey(Escort, on_delete=models.CASCADE, null=True, blank=True, default=None)
    DiseaseID = models.ForeignKey(Diseases, on_delete=models.CASCADE, null=True, blank=True, default=None)
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=100, blank=False)
    PhoneNumber = models.CharField(null=False, blank=False, max_length=100)
    Handel = models.CharField(max_length=100)
    ProfilePicture = models.ImageField(upload_to='photos%y%m%d')
    Male = models.BooleanField(default=True)
    Female = models.BooleanField(default=False)

    def __str__(self):
        return self.Handel

    class Meta:
        ordering = ['Handel']   





from django.db import models

class Medicine(models.Model):
    # DrugID = models.AutoField(primary_key=True)
    DrugName = models.CharField(primary_key=True,null=False, blank=True, max_length=50)
    purpose_of_use = models.CharField(max_length=50)
    Description = models.CharField(max_length=100)
    Duration_of_use = models.DateTimeField()
    number_of_times_day = models.IntegerField()
    type = models.CharField(max_length=100)
    expire_date = models.DateField(null=False, blank=True)
    Pillsnum = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.DrugName

    class Meta:
        ordering = ['DrugName']


class Reminder(models.Model):
    ReminderID = models.AutoField(primary_key=True)
    patientID = models.ForeignKey('patient', on_delete=models.CASCADE)
    DrugName = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='reminders_as_drugname')
    StartDate = models.DateTimeField()
    EndDate = models.DateTimeField()
    State = models.BooleanField(default=False)
    AlarmRecordes = models.TimeField()
    Audio = models.FileField(upload_to='audio/', default='default_audio.mp3')
    Notes = models.TextField(max_length=50)
    Checked = models.BooleanField(default=False)
    def __str__(self):
        return str(self.ReminderID)

    class Meta:
        ordering = ['ReminderID']





class Document(models.Model):
    DrugName = models.CharField(max_length=50)
    patientID = models.ForeignKey('patient', on_delete=models.CASCADE, null=False, blank=False,default=1)
    prescriptionID = models.AutoField(primary_key=True,null=False)
    exrays_test = models.ImageField(upload_to='photos/%Y/%m/%d')
    DiseasesID = models.ForeignKey('Diseases', on_delete=models.CASCADE, null=False, blank=False,default=1)
    EscortID = models.ForeignKey('Escort', on_delete=models.CASCADE, null=False, blank=False,default=1)

    def __str__(self):
        return str(self.patientID)

    class Meta:
        ordering = ['patientID']
