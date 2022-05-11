from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.utils.timezone import datetime
from customer.models import OrderModel

class Dashboard(LoginRequiredMixin,UserPassesTestMixin, View):
    def get(self, request, *args, **kwargs):
        #get currentdays
        today = datetime.today()
        orders = OrderModel.objects.filter(created_on__year=today.year, created_on__month=today.month, created_on__day=today.day)

        #loop through orders
        total_revenue = 0
        for order in orders:
            total_revenue += order.price

        #pas total number of orders
        context = {
            'orders': orders,
            'total_revenue': total_revenue,
            'total_orders': len(orders),
            }

        return render(request, 'restaurant/dashboard.html', context)

    def test_func(self):
        return self.request.user.groups.filter(name='LoJe').exists()
