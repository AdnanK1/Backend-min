from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DocumentSerializer
from .models import Document
from rest_framework.parsers import MultiPartParser,FormParser

# Create your views here.
class DocumentGenericAPIView(generics.ListCreateAPIView):
    parser_classes = [MultiPartParser,FormParser]
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
   

class DocumentDetailsGenericAPIView(generics.RetrieveUpdateDestroyAPIView):
    parser_classes = [MultiPartParser,FormParser]
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    lookup_field = 'slug'





