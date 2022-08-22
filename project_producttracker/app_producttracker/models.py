from django.db import models

# Create your models here.
class AppUser(models.Model):
    first_name = models.CharField(max_length=100)
    moddle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique = True)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'pt_users'

class Product(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    quantity = models.IntegerField()
    img = models.CharField(max_length=200, null = True, blank=True)
    category = models.CharField(max_length=100)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)

    class Meta:
        db_table = 'pt_products'