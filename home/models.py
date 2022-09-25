from django.db import models

# Create your models here.

class Contact(models.Model):
    username = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)

    def __str__(self):
        return self.username
class Emailcollection(models.Model):
    email = models.EmailField(max_length=122)
    def __str__(self):
        return self.email



