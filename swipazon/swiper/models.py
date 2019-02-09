from django.db import models
from products.models import Product

# Create your models here.
class Swiper(models.Model):

    # user fields
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    customer_id = models.CharField(max_length = 50)
    email = models.CharField(max_length = 70)

    class Meta:
        db_table = "Swipers"
    """
    liked_items = models.ForiegnKey(Product, on_delete=models.CASCADE)
    disliked_items = models.ManyToManyField(Product)
    purchased_items = models.ManyToManyField(Product)
    """

    # Attributes for handling data and stuff
    def get_next_item():
        """
        This function determines what the next item
        to be displayed to the user will be
        """
        return "hot dog"
