from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse


class Category(MPTTModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})

    class MPTTmeta:
        order_insertion_by = ['title']
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])

    

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to = 'uploads/', blank=True, null=True, verbose_name='Фотография продукта')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})
    
