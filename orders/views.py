from django.shortcuts import render
from django.views import View

from orders.models import get_all_orders, get_one_orders, search_orders


class Index(View):
    """
    Page index url/ or url/index
    """

    template_name = "orders/index.html"

    def get(self, request):
        """
        get in home page with list order
        """

        list_order = get_all_orders()

        return render(
            request,
            self.template_name,
            {
                "list_order": list_order
            },
        )

    def post(self, request, *args, **kwargs):
        """
        request post for search form
        """

        list_order = search_orders(search_text=request.POST['search_form'])
        return render(
            request,
            self.template_name,
            {
                "list_order": list_order
            },
        )


class Order(View):
    """
    get & display ONE order
    """

    template_name = "orders/order.html"

    def get(self, request, *args, **kwargs):
        """
        get one order & display
        """

        order = get_one_orders(id=kwargs['order_id'])

        return render(
            request,
            self.template_name,
            {
                "order": order
            },
        )
