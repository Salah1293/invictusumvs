from django.shortcuts import render
from rest_framework .response import Response

from users.decorators import roles_required
from .serializers import *
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
# Create your views here.


#FUNCTION TO REGISTER USERS
@api_view(['POST'])
def register_user(request):
    serializer = RegistrationSerializer(data=request.data)
    
    if serializer.is_valid():
        user = serializer.save()

        profile, created = Profile.objects.get_or_create(user=user)

        profile_serializer = ProfileSerializer(profile)

        return Response({
                'message': 'User Registered Successfully',
                'profile': profile_serializer.data,
        }, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#FUNCTION TO LOGIN A USER
@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        profile = user.profile
        roles = list(profile.role.values_list('name', flat=True))

        response = Response({
            'message': _('Login Successfully.'),
            'access_token': access_token,
            'roles': roles
        }, status=200)
        response.set_cookie('refresh_token', str(refresh), httponly=True, secure=True, samesite='Strict')

        return response
    else:
        if not User.objects.filter(username=username).exists():
            return Response({'error': _('Invalid Username')}, status=400)
        else:
            return Response({'error': _('Invalid Password')}, status=400)


#FUNCTION TO LOGOUT USER
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    response = Response({'message': 'User logged out successfully'}, status=200)
    response.delete_cookie('refresh_token')  
    return response



#FUNCTION TO LIST ALL ROLES
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@roles_required('admin')
def role_list(request):
    print('login user role is:', request.user.profile.role.name)
    roles = Role.objects.all()

    if roles.exists():
        data = RoleSerializer(roles, many=True).data
        return Response({'data': data}, status=status.HTTP_200_OK)
    
    else:
        return Response({'error': 'Roles not found.'}, status=status.HTTP_404_NOT_FOUND)
    


#FUNCTION TO GET A ROLE
@api_view(['GET'])
@roles_required('admin')
@permission_classes([IsAuthenticated])
def get_role(request, pk):
    try:
        role = Role.objects.get(pk=pk)
    except Role.DoesNotExist:
        return Response({'error': 'Role not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    data = RoleSerializer(role).data
    return Response({'data': data}, status=status.HTTP_200_OK)



#FUNCTION TO UPDATE A ROLE
@api_view(['PUT'])
@roles_required('admin')
@permission_classes([IsAuthenticated])
def update_role(request, pk): 
    try:
        role = Role.objects.get(pk=pk)
    except Role.DoesNotExist:
        return Response({'error': 'Role not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = RoleSerializer(role, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#FUNCTION TO CREATE A ROLE
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@roles_required('admin')
def create_role(request):
    serializer = RoleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


#FUNCTION TO DELETE A ROLE
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@roles_required('admin')
def delete_role(request, pk):
    try:
        role = Role.objects.get(pk=pk)
    except:
        return Response({'message': 'Role not found.'}, status=status.HTTP_404_NOT_FOUND)
    role.delete()
    return Response({'message': 'Role deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)

