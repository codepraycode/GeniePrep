from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.

class Users(models.Model):
    
    matric_number = models.CharField(
        max_length=50,
        unique=True,
        null=False,
        blank=False,
    )
    email = models.EmailField(
        max_length=100, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True);
    surname = models.CharField(max_length=255, blank=True,null=True)
    
    password = models.CharField(max_length=128)
    
    last_login = models.DateTimeField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.matric_number
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
    
    class Meta:
        ordering = ('matric_number')

    class Meta:
        db_table = "Users"
        verbose_name = "User"
        verbose_name_plural = "Users"
    
    
