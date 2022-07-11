from django.shortcuts import render
from django.views from View
from .models import Company
# Create your views here.
class companyView(View):

    def get(self,request):
        companies=compay.objects.all()
        if len(companies)>0:
            datos={'message':"Success",'companies':companies}



         def get(self,request):
        pass
         def post(self,request):
        pass
         def put(self,request):
        pass
         def delete(self,request):
        pass