from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from . models import Customers
from .serializers import customerserializer


# Create your views here.

@csrf_exempt
def get_cust(req):
    my_customers=Customers.objects.all()
    updated_data=customerserializer(my_customers,many=True)
    print(updated_data)
    return JsonResponse({"customers":updated_data.data})
  
  

 
@csrf_exempt
def reg_cust(req):
    data = json.loads(req.body)
    cust_data=customerserializer(data=data)
    new_customer=Customers.objects.create(
        id=data['id'],
        cust_name=data['cust_name'],
        mob=data['mob'],
        amount=data['amount'],
    )
    return HttpResponse ("successfully regiestered")
    

@csrf_exempt
def delete_customer(req,id):
    customer=Customers.objects.get(id=id)
    customer.delete()
    return HttpResponse("Customer deleted!",status=201)
    