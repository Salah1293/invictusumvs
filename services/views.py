from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
# Create your views here.




#LIST ALL SERVICES
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def services_list(request):
    try:
        service_list = Service.objects.all()
    except Service.DoesNotExist:
        raise NotFound('Services not found.')

    data = ServiceSerializer(service_list, many=True, context={'include_missions': True, 'include_approaches': False}).data
    return Response({'data': data})


#GET A SERVICE
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_service(request, pk):
    try:
        service = Service.objects.get(pk=pk)
    except Service.DoesNotExist:
        raise NotFound('Service not found.')
    
    data = ServiceSerializer(service, many=False, context={'include_missions': True, 'include_approaches': True}).data
    return Response({'data': data})


#CREATE A SERVICE
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_service(request):
    serializer = ServiceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#UPDATE A SERVICE
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_service(request, pk):
    try:
        service = Service.objects.get(pk=pk)
        print('service is:', service)
    except Service.DoesNotExist:
        print('where is service.')
        return Response({"error": "Service not found."}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ServiceSerializer(service, data=request.data, partial=True)  
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#DELETE A SERVICE
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_service(request, pk):
    try:
        service = Service.objects.get(pk=pk)
    except Service.DoesNotExist:
        return Response({'error': 'Service not found.'}, status=status.HTTP_404_NOT_FOUND)

    service.delete()
    return Response({'message': 'Service deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)




#LIST ALL MISSIONS
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def missions_list(request):
    try:
        missions = Mission.objects.all()
        
        if not missions.exists():
            return Response({'error': 'No missions found.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ServiceMissionSerializer(missions, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



#GET A MISSION
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_mission(request, pk):
    try:
        mission = Mission.objects.get(pk=pk)
    except Mission.DoesNotExist:
        return Response({'error': 'Mission not found.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ServiceMissionSerializer(mission)
    return Response({'data': serializer.data}, status=status.HTTP_200_OK)




#CREATE A MISSION
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_mission(request):
    serializer = ServiceMissionCreateUpdateSerializer(data=request.data)
    if serializer.is_valid():
        mission = serializer.save()
        return Response(
            {
                'message': 'Mission created successfully', 
                'mission': ServiceMissionCreateUpdateSerializer(mission).data
            }, 
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





#UPDATE A MISSION
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_mission(request, pk):
    try:
        mission = Mission.objects.get(pk=pk)
    except Mission.DoesNotExist:
        return Response({'error': 'Mission not found.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ServiceMissionCreateUpdateSerializer(mission, data=request.data, partial=True)
    if serializer.is_valid():
        updated_mission = serializer.save()
        return Response({'message': 'Mission updated successfully', 'mission': ServiceMissionCreateUpdateSerializer(updated_mission).data}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#DELETE A MISSION
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_mission(request, pk):
    try:
        mission = Mission.objects.get(pk=pk)
    except Mission.DoesNotExist:
        return Response({'error': 'Mission not found.'}, status=status.HTTP_404_NOT_FOUND)

    mission.delete()
    return Response({'message': 'Mission deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


