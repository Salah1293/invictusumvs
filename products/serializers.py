from rest_framework import serializers
from .models import *



#serialzer for robot type apis
class RobotTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RobotType
        fields = ['name', 'description', 'descriptive_name']


#serializer for robotComponent class that services robotCreatingSerializer for creating robot
class RobotComponentSerializer(serializers.ModelSerializer):
    component_model = serializers.PrimaryKeyRelatedField(queryset=ComponentModel.objects.all())

    class Meta:
        model = RobotComponent
        fields = ['component_model', 'quantity']


        
#serializer for listing robots 
class RobotSerialzier(serializers.ModelSerializer):
    # robot_type = RobotTypeSerializer()
    class Meta:
        model = Robot
        fields = ['version', 'description', 'manufacturer_date', 'status',
                   'descriptive_name', 'price', 'image', 'video']




#serializer for creating robot
class RobotCreateUpdateSerializer(serializers.ModelSerializer):
    components = RobotComponentSerializer(many=True)
    robot_type = serializers.PrimaryKeyRelatedField(queryset=RobotType.objects.all())

    class Meta:
        model = Robot
        fields = ['version', 'description', 'manufacturer_date', 'status', 'robot_type',
                   'descriptive_name', 'price', 'image', 'video', 'components']
        

    def validate_components(self, value):
        if not value:
            return serializers.ValidationError("At least one component must be chosen.")
        return value
        

    def create(self, validated_data):
        components_data = validated_data.pop('components')
        robot = Robot.objects.create(**validated_data)

        for component_data in components_data:
            component_model_instance = component_data.pop('component_model')
            RobotComponent.objects.create(robot_model=robot, component_model=component_model_instance, **component_data)

        return robot
            
        
    def update(self, instance, validated_data ):
        components_data = validated_data .pop('components')

        instance.version = validated_data .get('version', instance.version)
        instance.description = validated_data .get('description', instance.description)
        instance.manufacturer_date = validated_data.get('manufacturer_date', instance.manufacturer_date)
        instance.status = validated_data.get('status', instance.status)
        instance.robot_type = validated_data.get('robot_type', instance.robot_type)
        instance.descriptive_name = validated_data.get('descriptive_name', instance.descriptive_name)
        instance.price = validated_data.get('price', instance.price)
        instance.image = validated_data.get('image', instance.image)
        instance.video = validated_data.get('video', instance.video)
        instance.save()


        if components_data:
            instance.components.all().delete()
            for component_data in components_data:
                component_model_instance = component_data.pop('component_model')
                RobotComponent.objects.create(
                robot_model=instance,
                component_model=component_model_instance,
                **component_data
            )

        return instance




class ComponentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComponentType
        fields = ['name', 'description', 'descriptive_name']




class ComponentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComponentModel
        fields = ['model_name', 'specifications', 'price', 'component_type', 'descriptive_name']

        def validate_component_type(self, value):
            if not value:
                raise serializers.ValidationError('Component Type is required.')
            return value
        



class RobotStatusSerializer(serializers.Serializer):
    value = serializers.CharField()
    display_name = serializers.CharField()