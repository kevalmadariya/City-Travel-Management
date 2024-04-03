from django.db import models
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.

class AgentManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given username, email, and password.
        """
        if not username:
            raise ValueError('The Username must be set')
        if not email:
            raise ValueError('The Email must be set')
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
class Agent(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True,max_length=30,null=False,blank=False)
    agency_name  = models.CharField(unique=True,max_length=30,null=False,blank=False)
    email_id = models.EmailField(unique=True,null=False,blank=False)
    password = models.CharField(max_length=30,null=False,blank=False)
    gst_no = models.CharField(max_length=15)
    upi_id = models.CharField(max_length=30,null=False,blank=False)
    agency_logo = models.ImageField(upload_to='logo/',default='path/to/default/image.jpg')
    about_us = models.TextField()
    last_login = models.DateTimeField(auto_now=True)  # Add last_login field
    USERNAME_FIELD = 'username'  # Define the USERNAME_FIELD
    objects = AgentManager()


class AgentBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            agent = Agent.objects.get(username=username)
            if agent.check_password(password):
                return agent
        except Agent.DoesNotExist:
            return None

class TripPlan(models.Model):
     id = models.AutoField(primary_key=True)
     agency_id = models.ForeignKey(Agent,on_delete=models.CASCADE,to_field='id')
     trip_name = models.CharField(max_length=30,null=False,blank=False,unique=True)
     city = models.CharField(max_length=30,null=False,blank=False)
     price = models.FloatField(null=False,blank=False)
     capacity = models.IntegerField(null=False,blank=False)
     departure_date = models.DateField(null=False,blank=False)
     departure_time = models.TimeField(null=False,blank=False)
     departure_place = models.CharField(max_length=30,null=False,blank=False)
     return_date = models.DateField(null=False,blank=False)
     return_time = models.TimeField(null=False,blank=False)
     return_place = models.CharField(max_length=30,null=False,blank=False)
     duration = models.IntegerField(default=0)
     extra_info = models.TextField(default=None)     
     thumbnail = models.ImageField(upload_to='thumbnail/',default='path/to/default/image.jpg')
   


class Attraction(models.Model):
     id = models.AutoField(primary_key=True)
     trip_id = models.ForeignKey(TripPlan,on_delete=models.CASCADE,to_field='id') 
     name = models.CharField(max_length=30)
     att_imgs =  models.ImageField(upload_to='attraction/',default='path/to/default/image.jpg')

#traveler

class User(models.Model):
    id = models.AutoField(primary_key = True)
    username = models.CharField(max_length=30,null=False,blank=False)
    password = models.CharField(max_length=30,null=False,blank=False)
    dob = models.DateField()
    address = models.CharField(max_length=255)
    email = models.EmailField(max_length=50,null=False,blank=False)

class Ticket(models.Model):
    # id = models.CharField(max_length=30,primary_key = True)
    id = models.AutoField(primary_key=True)
    trip_id = models.ForeignKey(TripPlan,on_delete=models.CASCADE,to_field='id')
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,to_field='id')
    transaction_id = models.CharField(max_length=30,null=False,blank=False)

# class tempTicket(models.Model):
#     temp_id = models.AutoField(primary_key=True)
    
#     def __str__(self):
#         return f'{self.temp_id}'

class Passenger(models.Model):
    id = models.AutoField(primary_key=True)
    ticket_id = models.ForeignKey(Ticket,on_delete=models.CASCADE,to_field='id')
    # ticket_id = models.IntegerField()
    name = models.CharField(max_length=30,null=False,blank=False)
    age = models.IntegerField(null=False,blank=False)



