from django.core.serializers import serialize
from django.shortcuts import render
from .models import Klassi, Mehmonhona, Travel
from .serializer import TravelSerializer, KlassSerializer, HotelSerializer
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
# Create your views here.

class TravelView(APIView):
    def get(self, request: Request, pk=None):
        if pk:
            one = TravelSerializer(Travel.objects.get(pk=pk))
            return Response(one.data)

        objects = TravelSerializer(Travel.objects.all(), many=True)
        return Response(objects.data)


    def post(self, request: Request):
        serializer = TravelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


    def put(self, request: Request, pk: int):
        try:
            one = Travel.objects.get(pk=pk)
        except:
            return Response(status=404)

        serializer = TravelSerializer(one, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request: Request, pk:int):
        if pk:
            one = Travel.objects.get(pk=pk)
            one.delete()
            return Response({"message": "object has deleted!"})
        else:
            return Response({"message": "object not found! 404"})





class KlasView(APIView):
    def get(self, request: Request, pk=None):
        if pk:
            one = KlassSerializer(Klassi.objects.get(pk=pk))
            return Response(one.data)

        objects = KlassSerializer(Klassi.objects.all(), many=True)
        return Response(objects.data)


    def post(self, request: Request):
        serializer = KlassSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


    def put(self, request: Request, pk: int):
        try:
            one = Klassi.objects.get(pk=pk)
        except:
            return Response(status=404)

        serializer = KlassSerializer(one, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request: Request, pk:int):
        if pk:
            one = Klassi.objects.get(pk=pk)
            one.delete()
            return Response({"message": "object has deleted!"})
        else:
            return Response({"message": "object not found! 404"})






class HotelView(APIView):
    def get(self, request: Request, pk=None):
        if pk:
            one = HotelSerializer(Mehmonhona.objects.get(pk=pk))
            return Response(one.data)

        objects = HotelSerializer(Mehmonhona.objects.all(), many=True)
        return Response(objects.data)

    def post(self, request: Request):
        serializer = HotelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


    def put(self, request: Request, pk: int):
        try:
            one = Mehmonhona.objects.get(pk=pk)
        except:
            return Response(status=404)

        serializer = HotelSerializer(one, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request: Request, pk:int):
        if pk:
            one = Mehmonhona.objects.get(pk=pk)
            one.delete()
            return Response({"message": "object has deleted!"})
        else:
            return Response({"message": "object not found! 404"})