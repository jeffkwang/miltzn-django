from django.db import models
from django.utils import timezone, text

class Product(models.Model):
    name = models.CharField(max_length=255, null=False)
    subtitle = models.CharField(max_length=20, null=False)
    slug = models.SlugField(unique=True, null=True, blank=True)
    description = models.TextField(blank=True)
    images = models.JSONField(null=True, blank=True, default=list)  # Storing images as JSON
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(null=True, max_length=100, blank=True)
    stock_qty = models.IntegerField(null=True)
    tags = models.JSONField(default=list, blank=True)
    related_products = models.JSONField(default=list, blank=True)
    collections = models.JSONField(default=list, blank=True)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together=('name', 'color',)

    def save(self, *args, **kwargs):

        # Validation checks
        if self.price < 0 :
            raise ValueError("Price cannot be negative.")
        
        if self.stock_qty < 0:
            raise ValueError("Stock quantity cannot be negative.")
        
        if not self.name:
            raise ValueError("Product name is required.")

        if not self.slug:        
            self.slug = text.slugify(self.name) + "-" + text.slugify(self.subtitle)

        super().save(*args, **kwargs)

    def remove_from_store(self):
        
        # Soft delete functionality removes product from store display while keeping product in the database.
        
        if self.active == False:
            return
        else:
            self.active = False
            self.save()

    def permanent_delete(self, *args, **kwargs):
        
        # Permanently deletes product from database.
        
        super().delete(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("products-detail", kwargs={"pk": self.slug})
    
    def __str__(self):
        return self.name + " " + self.subtitle
    
class SeatCushion(Product):
    pass

class Pillow(Product):
    pass

class Rug(Product):
    pass

class WallArt(Product):
    pass

    