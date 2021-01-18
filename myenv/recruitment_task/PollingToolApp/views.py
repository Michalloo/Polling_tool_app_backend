from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from PollingToolApp.models import Response
from PollingToolApp.serializers import ResponseSerializer
# Create your views here.

@csrf_exempt
def responseApi(request,id =0):
    if request.method =='GET':
        responses = Response.objects.all()
        response_serializer  = ResponseSerializer(responses, many = True)
        return JsonResponse(response_serializer.data, safe = False)
        
    elif request.method == "POST":
        response_data = JSONParser().parse(request)
        response_serializer = ResponseSerializer(data = response_data)
        if response_serializer.is_valid():
            response_serializer.save()
            return JsonResponse("Your answer was saved succesfuly ",safe= False)
        return JsonResponse("Failed to add answer", safe= False)