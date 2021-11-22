""" Recover xml date in api and insert in DB """

from django.core.management.base import BaseCommand

from orders.models import insert_xml_data_in_db
from orders.tools import get_xml_data
from tools import logger


class Command(BaseCommand):
    help = "Insert data from API"

    def handle(self, *args, **kwargs):
        """
        get xml data & insert in db (sqlite)
        """

        logger.info('Récuperation des données XML')
        orders = get_xml_data.get_xml()
        if orders:
            logger.info('Insetion données XML dans la base de donnée')
            insert_xml_data_in_db(list_orders=orders)
