from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Building
from .serializers import BuildingSerializer
from rest_framework import filters
from rest_framework import status, viewsets
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.db.models import Q
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string, get_template
import string
import random
import string
from rest_framework.response import Response
class BuildingView(viewsets.ModelViewSet):  
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Building.objects.all()
    serializer_class=BuildingSerializer

    def create(self,request):
        res = request.data
        Building.objects.filter(~Q(formatID=res.get('formatID'))).delete()
        serializer = BuildingSerializer(data=res)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response()
        


