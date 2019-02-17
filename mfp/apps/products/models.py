from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(
        null=True, blank=True
    )
    parent = models.ForeignKey(
        'self', 
        related_name='parent', 
        on_delete=models.SET_NULL,
        null=True, 
        blank=True
    )


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(
        null=True, blank=True
    )
    price = models.FloatField()


    created = models.DateTimeField('Created date', auto_now_add=True)
    updated = models.DateTimeField('Updated date', auto_now=True)
    created_by = models.ForeignKey(
        User, 
        related_name='created_products', 
        on_delete=models.CASCADE,
        null=True, 
        blank=True
    )
    updated_by = models.ForeignKey(
        User, 
        related_name='updated_products', 
        on_delete=models.CASCADE,
        null=True, 
        blank=True
    )

