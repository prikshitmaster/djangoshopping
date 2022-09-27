from django.db import models

# Create your models here.
from home.models.catorgry import Catorgry


class Contact(models.Model):
    username = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)

    def __str__(self):
        return self.username
class Emailcollection(models.Model):
    email = models.EmailField(max_length=122)
    def __str__(self):
        return self.email

class AdminProduct(models.Model):
    name = models.CharField(max_length=122)
    desc = models.CharField(max_length=122)
    prize = models.IntegerField(default=0)
    catorgry = models.ForeignKey(Catorgry, on_delete=models.CASCADE,)
    image = models.ImageField(upload_to='static/uploadingimg')

    @staticmethod
    def get_all_product():
        AdminProduct.objects.all()

    def __str__(self):
        return self.name





