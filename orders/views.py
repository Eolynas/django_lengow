from django.shortcuts import render
from django.views import View


class Index(View):
    """
    Page index url/ or url/index
    """

    template_name = "orders/index.html"

    def get(self, request):
        """
        get in home page
        """

        return render(request, self.template_name)