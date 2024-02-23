from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = PhoneNumberField()
    address = models.CharField(max_length=100)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.email} {self.phone} {self.address}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField()
    image = models.ImageField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.description} {self.price} {self.count} {self.date_created}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.client.name} {self.products.all()} {self.total_price}'
