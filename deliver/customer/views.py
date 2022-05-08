from re import I
from django.shortcuts import render
from django.views import View

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')

class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/about.html')




#fra: https://www.youtube.com/watch?v=TXv2lbbhsOc&list=PLPSM8rIid1a0qiCpbfujex5lZoXr2SRFC&index=2