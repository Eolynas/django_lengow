from django.urls import path

from . import views

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("orders/<int:order_id>/", views.Order.as_view(), name="order"),
]