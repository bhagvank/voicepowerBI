from django.db import models
 
class Note(models.Model):
    text = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
   fname = models.CharField(max_length = 100)
   lname = models.CharField(max_length = 100)
   country = models.CharField(max_length = 100,null=True)
   picture = models.ImageField(upload_to = 'pictures')

   class Meta:
      db_table = "profile"
        
import datetime

from django.db import models
from django.utils import timezone
import os

# Create your models here.


class AIRecruiterUser(models.Model):
    """
    AIRecruiterUser User models

    """
    
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    
    def _str_(self):
      """
       str method
       Returns
      -----------
       str
         username
      """
      return self.username

    
    def authenticate(self,username,password):
        """
        authenticate method
        Parameters
        ----------
        username : str
         user name
        password : str
           password  
         Returns
         -----------
          bool
           true if authentication is successful and false if it fails.
         """

        check = None
        error_username = self._validate_username(username)
        error_password = self._validate_password(password)
        if error_username == None and error_password == None:
           check = True
        else :
           check = False              
        return check,error_username,error_password

    def _validate_username(self,username):
        error_username = None
        if self.username != username:
           error_username = "InValid UserName" 

        return error_username

    def _validate_password(self, password):
        error_password = None
        if self.password != password: 
           error_password = "InValid Password"
        return error_password   


          
        