from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length=250, unique=True)
	slug = models.SlugField(max_length=250, unique=True)
	description = models.TextField(blank=True)
	image = models.ImageField(upload_to='category', blank=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def get_url(self):
		return reverse('shop:products_by_category', args=[self.slug])

	def __str__(self):
		return str(self.name)

class Product(models.Model):
	name = models.CharField(max_length=250, unique=True)
	slug = models.SlugField(max_length=250, unique=True)
	description = models.TextField(blank=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	price = models.DecimalField(default='$', max_digits=10, decimal_places=2)
	unit = models.CharField(max_length=10, null=True)
	image = models.ImageField(upload_to='product', blank=True, null=True)
	stock = models.IntegerField()
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'product'
		verbose_name_plural = 'products'

	def get_url(self):
		return reverse('shop:ProdCatDetail', args=[self.category.slug, self.slug])

	def __str__(self):
		return str(self.name)
	
	def get_rating(self):
		reviews_total = 0

		for review in self.reviews.all():
			reviews_total += review.rating

		if reviews_total > 0:
			return reviews_total / self.reviews.count()
		
		return 0

class Review(models.Model):
	product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
	rating = models.IntegerField(default=3)
	content = models.TextField()
	created_by = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)