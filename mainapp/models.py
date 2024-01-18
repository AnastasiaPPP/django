from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    date_of_registration = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}, {self.email}, {self.phone_number}, {self.address}, {self.date_of_registration}'


class Good(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    count = models.IntegerField()
    date_of_add = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}, {self.description}, {self.price}, {self.count}, {self.date_of_add}'


class Order(models.Model):
    client_id = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    goods = models.ManyToManyField(Good)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.client_id}, {self.goods}, {self.total_price}, {self.date}'

