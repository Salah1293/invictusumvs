from rest_framework import serializers
from .models import *


#serializer for approaches
class MissionApproachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Approach
        fields = ['id', 'title', 'description']


#serializer for missions
class ServiceMissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = ['id', 'name', 'description']



#serializer to get missions with approaches to within service
class ServiceMissionWithApproachSerializer(serializers.ModelSerializer):

    approaches = serializers.SerializerMethodField()

    class Meta:
        model = Mission
        fields = ['id', 'name', 'description', 'approaches']

    def get_approaches(self, obj):
        if self.context.get('include_approaches', False):
            return MissionApproachSerializer(obj.approaches.all(), many=True).data
        else:
            return None


#serializer to services
class ServiceSerializer(serializers.ModelSerializer):

    missions = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = ['id', 'name', 'description', 'missions']

    def get_missions(self, obj):
        if self.context.get('include_missions', False):
            return ServiceMissionWithApproachSerializer(obj.missions.all(), many=True, context=self.context).data
        else:
            return ServiceMissionSerializer(obj.missions.all(), many=True).data 



#serializer to create and update missions 
class ServiceMissionCreateUpdateSerializer(serializers.ModelSerializer):
    approaches = MissionApproachSerializer(many=True, required=False)
    service = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all())  

    class Meta:
        model = Mission
        fields = ['name', 'description', 'approaches', 'service']  

    def create(self, validated_data):
        approaches_data = validated_data.pop('approaches', [])
        service = validated_data.pop('service') 
        mission = Mission.objects.create(service=service, **validated_data)  

        for approach_data in approaches_data:
            Approach.objects.create(mission=mission, **approach_data)

        return mission

    def update(self, instance, validated_data):
        approaches_data = validated_data.pop('approaches', [])
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)

        if 'service' in validated_data:
            instance.service = validated_data.get('service', instance.service) 

        instance.save()

        instance.approaches.all().delete()
        for approach_data in approaches_data:
            Approach.objects.create(mission=instance, **approach_data)

        return instance


