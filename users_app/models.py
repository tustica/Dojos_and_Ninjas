from os import name
from django.db import models
from django.db.models.fields import related

class users(models.Model):
    def __repr__(self):
        return f"<user object: {self.first_name} {self.last_name}>"

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class dojos(models.Model):
    dojo_name = models.CharField(max_length=255)
    dojo_city = models.CharField(max_length=255)
    dojo_state = models.CharField(max_length=2)

class ninjas(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(dojos, related_name="dojo", on_delete=models.CASCADE)

