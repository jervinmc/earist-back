from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Room
from .serializers import RoomSerializer
from rest_framework import filters
from rest_framework import status, viewsets
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string, get_template
import string
import random
import string
from django.db.models import Q
from rest_framework.response import Response
class RoomView(viewsets.ModelViewSet):  
    filter_backends = [filters.SearchFilter]
    search_fields = ['tiles']
    queryset=Room.objects.all()
    serializer_class=RoomSerializer

    def create(self,request):
        res = request.data
        Room.objects.filter(~Q(formatID=res.get('formatID')),building_name=res.get('building_name'),floor=res.get('floor')).delete()
        serializer = RoomSerializer(data=res)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response()
    



    # def list(self,request):
    #     print(request.query_params.get('building_name'))
    #     item = Room.objects.filter(building_name=request.query_params.get('building_name'),floor=request.query_params.get('floor'))
    #     item = RoomSerializer(item,many=True)
    #     return Response(data=item.data)


class RoomBuilding(generics.GenericAPIView):
    def get(self,request,format=None,user_id=None):
        print(request.query_params.get('building_name'))
        item = Room.objects.filter(building_name=request.query_params.get('building_name'),floor=request.query_params.get('floor'))
        item = RoomSerializer(item,many=True)
        return Response(data=item.data)