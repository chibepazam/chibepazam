from django.contrib import auth
from django.db import models


class Food(models.Model):
    """A food."""
    name = models.CharField(max_length=70,
                             help_text="The name of the food.")
    ingredients = models.ManyToManyField('Ingredient',
                                          through="FoodIngredient")
    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """A food ingredients."""
    name = models.CharField(max_length=50,
                                   help_text="The ingredient name.")
    def __str__(self):
        return self.name

class FoodIngredient(models.Model):
    """ An intermediate table to connect food and ingredient."""
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

