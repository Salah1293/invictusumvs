from django.db import models
import uuid

# Create your models here.



class Service(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300, unique=True, blank=False)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Service'
    

class Mission(models.Model):
    id = models.AutoField(primary_key=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='missions')
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Mission'

    

class MissionImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='media/mission_images', default='default.jpg')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Image for {self.mission.name}.'
    
    class Meta:
        db_table = 'MissionImage'
    

class MissionVideo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name='videos')
    video = models.FileField(upload_to='media/mission_videos')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Video for {self.mission.name}'
    
    class Meta:
        db_table = 'MissionVideo'


class Approach(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name='approaches')
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Approach {self.title} of mission {self.mission.name}"
    
    class Meta:
        db_table = 'Approach'
    

class Feature(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    approach = models.ForeignKey(Approach, on_delete=models.CASCADE, related_name='features')
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (f"Feature {self.title} of approach {self.approach.title}"
                 f"of mission {self.approach.mission.name}")
                 
    
    class Meta:
        db_table = 'Feature'
