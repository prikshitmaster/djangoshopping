from django.db import models

# Create your models here.

class Catorgry(models.Model):
    name = models.CharField(max_length=122)

    @staticmethod
    def get_all_categories():
        Catorgry.objects.all()

    def __str__(self):
        return self.name