from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    phone = models.CharField(max_length=30, null=True, blank=True)
    image = models.ImageField(upload_to='images/accounts', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'accounts'
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
        
    def __str__(self):
        """
        Return a string representation of the Account object.

        This method overrides the default `__str__` method of the Account class. It returns a string representation of the Account object by concatenating the `first_name` and `last_name` attributes of the object. If the `last_name` attribute is None or empty, it returns only the `first_name` attribute.

        Returns:
            str: A string representation of the Account object.
        """
        
        return f"{self.first_name} {self.last_name}" if self.last_name else self.first_name