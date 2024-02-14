from django.db import models


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=70, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)

    class Meta:
        db_table = "category"

    def __str__(self):
        return self.name


class Products(models.Model):
    class Meta:
        db_table = "product"

    name = models.CharField(max_length=70, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="goods_images", blank=True, null=True)
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
