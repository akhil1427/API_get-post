from django.shortcuts import render
from app.models import *
from rest_framework.decorators import APIView
from app.Serializers import *
from rest_framework.response import Response

# Create your views here.

class productcurd(APIView):
    def get(self,request):
        PDO=Product.objects.all()
        PJD=ProductSerializer(PDO,many=True)
        return Response(PJD.data)

    def post(self,request):
        JDO=request.data
        PDJO=ProductSerializer(data=JDO)
        if PDJO.is_valid():
            PDJO.save()
            return Response({'insert':'Data is inserted successfully'})
        else:
            return Response({'insert':'Data is not inserted'})
