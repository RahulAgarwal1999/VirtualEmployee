from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class UserDetails(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    user_phone = PhoneNumberField(null=False, blank=False, unique=False, default='+91')
    user_pass = models.CharField(max_length=10, blank=True)


    def __str__(self):
        return str(self.user_id) if self.user_id else ''



# class UserProfile(models.Model):
#
# 	user_id = models.ForeignKey(User,on_delete=models.CASCADE)
# 	user_profile 		 = models.ImageField(upload_to='user_profile/')
# 	gender               = models.CharField(max_length=50)
# 	address              = models.CharField(max_length=200)
# 	degree               = models.CharField(max_length=50)
# 	specialisation       = models.CharField(max_length=50)
# 	current_year 	     = models.CharField(max_length=50)
# 	institution_name     = models.CharField(max_length=100)
# 	institution_address  = models.CharField(max_length=200)
# 	career_category      = models.CharField(max_length=50)
# 	career_specification = models.CharField(max_length=50)
#
# 	def __str__(self):
# 		return str(self.first_name+" "+self.last_name)
	 


