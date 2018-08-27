from django.db import models
from django.urls import reverse

class Product(models.Model):

	name = models.CharField(max_length=150, null=False)
	cost = models.FloatField(default=0.0)
	month_cost = models.FloatField(default=0.0)
	description = models.TextField(max_length=400, null=False)
	image = models.ImageField(null=True)
	available = models.BooleanField(default=False)
	TYPES_OF_PRODUCT = (
		(0, 'New product'),
		(1, 'Subscription'),
	)
	type = models.IntegerField(choices=TYPES_OF_PRODUCT, default=0)


	class Meta:
		ordering = ['-id']


	def __str__(self):
		return "%s (%s) cost: %s, m.cost: %s" % (self.id,self.name,self.cost,self.month_cost)


	def get_absolute_url(self):
		return reverse('product-detail', args=[str(self.id)])


# class Invoice(models.Model):
# 	