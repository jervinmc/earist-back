from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Floor
from .serializers import FloorSerializer
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
from rest_framework.response import Response
class FloorView(viewsets.ModelViewSet):  
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Floor.objects.all()
    serializer_class=FloorSerializer
        


