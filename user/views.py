from django.shortcuts import render, get_object_or_404

from rest_framework import response, permissions, views, viewsets, generics, mixins

from django.conf import settings
from user import models, serializers

# Create your views here.

class HealthView(views.APIView):    
    
    permission_classes = (permissions.AllowAny, )

    def get(self, request):
        return response.Response({"health": True})
    
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.AllowAny]

    
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer