from django.urls import path
from swiper import views


urlpatterns = [
    path('', views.SwiperView.as_view(), name="user-data")
    ]
