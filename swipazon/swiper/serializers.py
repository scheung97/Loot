from rest_framework import serializers

from .models import Swiper

class SwiperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Swiper
        fields = ("first_name", "last_name", "customer_id",
                "disliked_items", "liked_items", "cart_items",
                "next_item")
