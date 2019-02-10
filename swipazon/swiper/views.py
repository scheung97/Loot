# swiper/views.py

from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Swiper
from .serializers import SwiperSerializer
from products.models import Product

import random

class SerializedSwiperView(generics.ListAPIView):
    queryset = Swiper.objects.all()
    serializer_class = SwiperSerializer

class SwiperView(generics.ListAPIView):
    queryset = Swiper.objects.all()
    serializer_class = SwiperSerializer

    def get(self, request):
        print(request.query_params)
        swipers = Swiper.objects.all()

        data = SwiperSerializer(swipers, many=True).data
        return Response(data)

    def post(self, request):
        query_params = request.query_params
        customer_id = query_params["customer_id"]
        swipe_direction = query_params["swipe_direction"]
        product_id = query_params["product_id"]

        update_model_controller(customer_id, swipe_direction, product_id)

        swipers = Swiper.objects.all()
        data = SwiperSerializer(swipers, many=True).data
        return Response("Nice - Now do a get")

def update_model_controller(customer_id, swipe_direction, product_id):
    disliked_items = [x for x in Swiper.objects.get(customer_id=customer_id).disliked_items.values()]
    liked_items = [x for x in Swiper.objects.get(customer_id=customer_id).liked_items.values()]
    cart_items = [x for x in Swiper.objects.get(customer_id=customer_id).cart_items.values()]
    # all these items look like {'id':3 , 'name': 'not hotdog', 'product_id':3}
    # import pdb; pdb.set_trace()
    print(f"disliked items {Swiper.objects.get(customer_id=customer_id).disliked_items.values()}")
    all_swiped_items = [x["product_id"] for x in disliked_items] \
            + [x["product_id"] for x in liked_items] \
            + [x["product_id"] for x in cart_items]

    print(all_swiped_items)

    new_product = Product.objects.get(product_id=product_id)

    SwiperObject = Swiper.objects.get(customer_id=customer_id)

    # update list of products already seen
    if swipe_direction == 'left':
        SwiperObject.disliked_items.add(new_product)
    if swipe_direction == 'right':
        Swiper.objects.filter(customer_id=customer_id).liked_items.add(new_product)

    if swipe_direction == 'up':
        Swiper.objects.filter(customer_id=customer_id).cart_items.add(new_product)

    # get next product id
    all_product_ids = [str(x) for x in range(1, 10)]

    found_item = False
    for id in all_product_ids:
        if id not in all_swiped_items:
            print(id)
            print(all_swiped_items)
            Swiper.objects.filter(customer_id=customer_id).update(next_item=id)
            found_item = True
            break


    if not found_item:
        id = random.choice(all_product_ids)
        Swiper.objects.filter(customer_id=customer_id).update(next_item=id)
