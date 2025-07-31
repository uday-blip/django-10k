from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from .serializers import studentSerializers
from django.views.decorators.csrf import csrf_exempt
import json
from . models import Students


# Create your views here.

def ready(req):
    return HttpResponse("working")

@csrf_exempt
def reg_stu(req):
    req_data=json.loads(req.body)
    serializer=studentSerializers(data=req_data)
    
    if serializer.is_valid():
       serializer.save()
       return HttpResponse("registeration succesfull",status=200)
    else:
        return HttpResponse("invalid data",status=400)
    
    
@csrf_exempt
def see_stu(req):
    stu_data=Students.objects.all()
    serializer=studentSerializers(stu_data,many=True)
    return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def get_stud(req,sid):
    if req.method == "GET":
       try:
           stu_details=Students.objects.get(id=sid)
           serial=studentSerializers(stu_details)
           return JsonResponse({"data":serial.data},status=200)
       except Students.DoesNotExist:
           return HttpResponse("no student found")
       except Exception as e:
           return HttpResponse("failed to get",status=404)
       
@csrf_exempt
def tc(req,sid):
    if req.method == "DELETE":
        try:
            student=Students.objects.get(id=sid)
            tc_stu=studentSerializers(student)
            student.delete()
            return HttpResponse("deletion over")
        except Students.DoesNotExist:
            return HttpResponse("not found")
        except Exception as e :
            return HttpResponse("only delete method is allowed")