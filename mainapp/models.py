from django.db import models

class Tarif(models.Model):
    name = models.CharField(max_length=50)
    users = models.ManyToManyField('Client', through='Operator')

    def __str__(self):
        return self.name

class Sity(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=50)
    sity_name = models.ForeignKey(Sity, on_delete=models.SET_NULL, null=True)
    tarifs = models.ManyToManyField(Tarif, through='Operator')

    def __str__(self):
        return self.name

class Operator(models.Model):
    name = models.CharField(max_length=50)
    tarif = models.ForeignKey(Tarif, on_delete=models.CASCADE, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name + '/' + self.client.name
