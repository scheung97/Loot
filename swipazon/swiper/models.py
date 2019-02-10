#

from django.db import models
from products.models import Product

DEFAULT_PRODUCT_ID = 1

# Create your models here.
class Swiper(models.Model):

    # user fields
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    customer_id = models.CharField(max_length = 50)
    email = models.CharField(max_length = 70)
    next_item = models.CharField(max_length = 70)

    class Meta:
        db_table = "Swipers"

    liked_items = models.ManyToManyField(Product, default = DEFAULT_PRODUCT_ID, related_name = 'liked_items')
    disliked_items = models.ManyToManyField(Product, default = DEFAULT_PRODUCT_ID, related_name = 'disliked_items')
    cart_items = models.ManyToManyField(Product, default = DEFAULT_PRODUCT_ID, related_name = 'cart_items')
