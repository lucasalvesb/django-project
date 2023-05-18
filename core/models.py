from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.name, self.age, self.cpf, self.email, self.phone, self.address
    
