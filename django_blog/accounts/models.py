from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator


# Create your models here.
class CustomUser(AbstractUser):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        max_length=16,
        unique=True,
        validators=[username_validator],
    )
    
    last_name = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    date_of_birth = models.DateField(blank=True, null=True)
    email = models.EmailField(max_length=254,unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    profile = models.ImageField(null=True,blank=True,default='unknown.jpg')
    introduction = models.TextField(max_length=150,null=True,blank=True)
    


    REQUIRED_FIELDS = ['email','password']
    def __str__(self):
            return self.username
    

# class Follow(models.Model):
#       follow = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name= 'follwing_user')
#       follow_target = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='followed_by_user')

# class Block(models.Model):
#       block = models.ForeignKey(CustomUser,on_delete=models.CASCADE = 'blocking_user',related_name= 'blocking_user')
#       block_target = models.ForeignKey(CustomUser,on_delete=models.CASCADE = 'blocked_by_user'related_name='blocked_by_user')