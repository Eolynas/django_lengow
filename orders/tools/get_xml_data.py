import requests
import xmltodict as xmltodict
from typing import Union


def get_xml() -> Union[list, None]:
    """
    request for get data xml
    :return: list orders
    """

    response = requests.get("http://test.lengow.io/orders-test.xml")

    if response.status_code != 200:
        return None
    dict_data = xmltodict.parse(response.content)

    orders_list = []
    for order in dict_data['statistics']['orders']['order']:
        order_dict = {
            'order_id': order['order_id'],
            'marketplace': order['marketplace'],
            'billing_firstname': order['billing_address']['billing_firstname'],
            'billing_lastname': order['billing_address']['billing_lastname'],
            'billing_address': order['billing_address']['billing_address'],
            'billing_address_complement': order['billing_address']['billing_address_complement'],
            'billing_city': order['billing_address']['billing_city']
        }

        if isinstance(order['billing_address']['billing_zipcode'], int):
            order_dict['billing_zipcode'] = order['billing_address']['billing_zipcode']
        else:
            order_dict['billing_zipcode'] = None

        for index, value in order_dict.items():
            if value == 'None':
                order_dict[index] = None
        orders_list.append(order_dict)
    return orders_list
