from django.db import models
from django.db.models import Q


class Orders(models.Model):
    """
    models categories
    """

    order_id = models.CharField(max_length=200, null=False, unique=True)
    marketplace = models.CharField(max_length=200, null=True)
    billing_firstname = models.CharField(max_length=50, null=True)
    billing_lastname = models.CharField(max_length=50, null=True)
    billing_address = models.CharField(max_length=200, null=True)
    billing_address_complement = models.CharField(max_length=200, null=True)
    billing_zipcode = models.IntegerField(null=True)
    billing_city = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(null=False, auto_now_add=True)

    class Meta:
        verbose_name_plural = "orders"


def insert_xml_data_in_db(list_orders):
    """
    insert data in db (sqlite)
    :param list_orders: list of orders
    """

    for order in list_orders:

        order_obj, created = Orders.objects.update_or_create(
            order_id=order['order_id']
        )

        order_obj.marketplace = order['marketplace']
        order_obj.billing_firstname = order['billing_firstname']
        order_obj.billing_lastname = order['billing_lastname']
        order_obj.billing_address = order['billing_address']
        order_obj.billing_address_complement = order['billing_address_complement']
        if not order['billing_zipcode'] is None:
            order_obj.billing_zipcode = order['billing_zipcode']
        else:
            order_obj.billing_zipcode = None
        order_obj.billing_city = order['billing_city']

        order_obj.save()


def get_all_orders() -> list:
    """
    get all orders in DB
    :return: list orders
    """
    orders = Orders.objects.all()

    return orders


def get_one_orders(id: int) -> Orders:
    """
    get one orders in DB by id
    :param id: id in DB (not a order_id) -> int
    :return: one order
    """
    orders = Orders.objects.filter(id=id).first()

    return orders


def search_orders(search_text: str) -> list:
    """
    search list orders by one or more work
    :param search_text:
    :return: list order
    """

    # TODO: Condition sur l'int pour éviter les problemes avec le zipcode
    if isinstance(search_text, int):
        list_orders = Orders.objects.filter(
            Q(marketplace__icontains=search_text) |
            Q(billing_firstname__icontains=search_text) |
            Q(billing_lastname__icontains=search_text) |
            Q(billing_address__icontains=search_text) |
            Q(billing_address_complement__icontains=search_text) |
            Q(billing_zipcode=search_text) |
            Q(billing_city__icontains=search_text)
        ).all()
    else:
        list_orders = Orders.objects.filter(
            Q(marketplace__icontains=search_text) |
            Q(billing_firstname__icontains=search_text) |
            Q(billing_lastname__icontains=search_text) |
            Q(billing_address__icontains=search_text) |
            Q(billing_address_complement__icontains=search_text) |
            # Q(billing_zipcode=search_text) |
            Q(billing_city__icontains=search_text)
        ).all()

    return list_orders
