""" Recover xml date in api and insert in DB """
import os

from django.core.management.base import BaseCommand

from tools import logger

from orders.tools import get_xml_data
from orders.models import insert_xml_data_in_db


class Command(BaseCommand):
    help = "Insert data from API"

    def handle(self, *args, **kwargs):
        """
        get xml data & insert in db (sqlite)
        """

        print("INSERTION")
        orders = get_xml_data.get_xml()
        insert_xml_data_in_db(list_orders=orders)
        print("stop")