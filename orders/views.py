from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
# Create your views here.



#FUNCTION TO CREATE AN ORDER
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_order(request):
    serializer = OrderSerializer(data=request.data)
    
    if serializer.is_valid():
        order = serializer.save(profile_id=request.user.profile)  
        return Response({'message': 'Order created successfully.', 'order_id': order.id}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)