from django.db import models


class Category(models.Model):
	name = models.CharField(unique=True, max_length=50)
	description = models.CharField(blank=True, max_length=200)

	def __str__(self):
		return "%s" % self.name


class Dish(models.Model):
	name = models.CharField(unique=True, max_length=50)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	description = models.CharField(blank=True, max_length=200)
	price = models.FloatField(blank=True)

	def __str__(self):
		return "%s $%s" % (self.name, self.price)