from django.db import models
from django.utils.encoding import python_2_unicode_compatible

class lesson(models.Model):
	"""docstring for lesson"""
	year = models.DecimalField(max_digits=4,decimal_places=0)
	name = models.CharField(max_length=20)
	ID1 = models.CharField(max_length=10)
	school = models.CharField(max_length=10)
	teacher = models.CharField(max_length=5)
	time  = models.CharField(max_length=20)

	def __str__(self):
		return self.name
