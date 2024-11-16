from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes

from users.decorators import roles_required
from .serializers import *
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated




#LIST ALL ROBOT TYPES
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@roles_required('admin')
def robot_type_list(request):
    robot_type_list = RobotType.objects.all()
        
    if robot_type_list.exists():
        data = RobotTypeSerializer(robot_type_list, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Robot Types not found.'}, status=status.HTTP_404_NOT_FOUND)
    

#GET A ROBOT TYPE
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@roles_required('admin')
def get_robot_type(request, pk):
    try:
        robot_type = RobotType.objects.get(pk=pk)
    except RobotType.DoesNotExist:
        return Response({'error': 'Robot Type not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    data = RobotTypeSerializer(robot_type).data
    return Response(data, status=status.HTTP_200_OK)


#CREATE A ROBOT TYPE
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@roles_required('admin')
def create_robot_type(request):
    serializer = RobotTypeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#UPDATE A ROBOT TYPE
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@roles_required('admin')
def update_robot_type(request, pk):
    try:
        robot_type = RobotType.objects.get(pk=pk)
    except RobotType.DoesNotExist:
        return Response({'error': 'Robot Type not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = RobotTypeSerializer(robot_type, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#DELETE A ROBOT TYPE
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@roles_required('admin')
def delete_robot_type(request, pk):
    try:
        robot_type = RobotType.objects.get(pk=pk)
    except RobotType.DoesNotExist:
        return Response({'error': 'Robot Type not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    robot_type.delete()
    return Response({'message': 'Robot Type deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)



#LIST ALL ROBOT
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def robot_list(request):
    robot_list = Robot.objects.all()

    if robot_list.exists():
        data = RobotSerialzier(robot_list, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Robot not found.'}, status=status.HTTP_404_NOT_FOUND)
    

#GET A ROBOT
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_robot(request, pk):
    try:
        robot = Robot.objects.get(pk=pk)
    except Robot.DoesNotExist:
        return Response({'error': 'Robots not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    data = RobotSerialzier(robot).data
    return Response(data, status=status.HTTP_200_OK)


#UPDATE A ROBOT
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@roles_required('admin')
def update_robot(request, pk):
    try:
        robot = Robot.objects.get(pk=pk)
    except Robot.DoesNotExist:
        return Response({'error': 'Robot not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = RobotCreateUpdateSerializer(robot, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#CREATE A ROBOT
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@roles_required('admin')
def create_robot(request):
    serializer = RobotCreateUpdateSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#DELETE A ROBOT
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@roles_required('admin')
def delete_robot(request, pk):
    try:
        robot = Robot.objects.get(pk=pk)
    except Robot.DoesNotExist:
        return Response({'error': 'Robot not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    robot.delete()
    return Response({'message': 'Robot deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


#LIST ALL COMPONENT TYPES
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@roles_required('admin')
def component_type_list(request):
    component_type_list = ComponentType.objects.all()

    if component_type_list.exists():
        data = ComponentTypeSerializer(component_type_list, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'component types not found.'}, status=status.HTTP_404_NOT_FOUND)
    

#GET A COMPONENT TYPE
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@roles_required('admin')
def get_component_type(request, pk):
    try:
        component_type = ComponentType.objects.get(pk=pk)
    except ComponentType.DoesNotExist:
        return Response({'error': 'component type not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    data = ComponentTypeSerializer(component_type).data
    return Response(data, status=status.HTTP_200_OK)


#UPDATE COMPONENT TYPE
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@roles_required('admin')
def update_component_type(request, pk):
    try:
        component_type = ComponentType.objects.get(pk=pk)
    except ComponentType.DoesNotExist:
        return Response({'error': 'Component Type not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ComponentTypeSerializer(component_type, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


#CREATE A COMPONENT TYPE
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@roles_required('admin')
def create_component_type(request):
    serializer = ComponentTypeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#DELETE A COMPONENT TYPE
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@roles_required('admin')
def delete_component_type(request, pk):
    try:
        component_type = ComponentType.objects.get(pk=pk)
    except ComponentType.DoesNotExist:
        return Response({'error': 'Component Type not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    component_type.delete()
    return Response({'message': 'Component Type deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)



#LIST ALL COMPONENT MODELS
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def component_model_list(request):
    component_model_list = ComponentModel.objects.all()

    if component_model_list.exists():
        data = ComponentModelSerializer(component_model_list, many=True).data
        return Response({'data': data}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Component Model not found.'}, status=status.HTTP_404_NOT_FOUND)
    


#GET A COMPONENT MODEL
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_component_model(request, pk):
    try:
        component_model = ComponentModel.objects.get(pk=pk)
    except ComponentModel.DoesNotExist:
        return Response({'error': 'Component Model not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    data = ComponentModelSerializer(component_model).data
    return Response({'data': data}, status=status.HTTP_200_OK)



#CREATE A COMPONENT MODEL
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@roles_required('admin')
def create_component_model(request):
    serializer = ComponentModelSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#UPDATE A COMPONENT MODEL
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@roles_required('admin')
def update_component_model(request, pk):
    try:
        component_model = ComponentModel.objects.get(pk=pk)
    except ComponentModel.DoesNotExist:
        return Response({'error': 'Component Model not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ComponentModelSerializer(component_model, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




#DELETE A COMPONENT MODEL
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@roles_required('admin')
def delete_component_model(request, pk):
    try:
        component_model = ComponentModel.objects.get(pk=pk)
    except ComponentModel.DoesNotExist:
        return Response({'error': 'Component Model not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    component_model.delete()
    return Response({'message': 'Component Model deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)



#GET ROBOT STATUSES TO SERVE CREATING ROBOT API
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@roles_required('admin')
def list_robot_statuses(request):
    try:
        status_choices = Robot.STATUS_CHOICES

        status_data = [{'value': value, 'display_name': display_name} for value, display_name in status_choices]

        serializer = RobotStatusSerializer(status_data, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
