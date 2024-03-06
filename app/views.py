from django.shortcuts import render
from app.models import *
from rest_framework.decorators import APIView
from app.Serializers import *
from rest_framework.response import Response

# Create your views here.

class productcurd(APIView):
    def get(self,request,id):
        PDO=Product.objects.all()
        PJD=ProductSerializer(PDO,many=True)
        return Response(PJD.data)

    def post(self,request,id):
        JDO=request.data
        PDJO=ProductSerializer(data=JDO)
        if PDJO.is_valid():
            PDJO.save()
            return Response({'insert':'Data is inserted successfully'})
        else:
            return Response({'insert':'Data is not inserted'})

    def put(self,request,id):
        PO=Product.objects.get(id=id)
        UPDO=ProductSerializer(PO,data=request.data)
        if UPDO.is_valid():
            UPDO.save()
            return Response({'update':'Data is Updated'})
        else:
            return Response({'error':'Update not done'})

    def patch(self,request,id):
        POO=Product.objects.get(id=id)
        UDO=ProductSerializer(POO,data=request.data,partial=True)
        if UDO.is_valid():
            UDO.save()
            return Response({'update':'Data is Updated'})
        else:
            return Response({'error':'Update not done'})

    def delete(self,request,id):
        Product.objects.get(id=id).delete()
        return Response({'delete':'Data is deleted'})


    
