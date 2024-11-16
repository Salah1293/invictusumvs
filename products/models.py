from django.db import models

# Create your models here.


class RobotType(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=400, unique=True)
    descriptive_name = models.CharField(max_length=400, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'RobotType'


class Robot(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('in_maintenance', 'In Maintenance'),
        ('deployed', 'Deployed'),
        ('decommissioned', 'Decommissioned'),
        ('reserved', 'Reserved')
    ]

    id = models.AutoField(primary_key=True, unique=True)
    robot_type = models.ForeignKey(RobotType, on_delete=models.CASCADE, related_name='robots')
    version = models.CharField(max_length=200, unique=True)
    descriptive_name = models.CharField(max_length=400, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    manufacturer_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='available')
    price = models.FloatField(blank=True, null=True)
    image = models.ImageField(upload_to='robots/images/', null=True, blank=True)
    video = models.FileField(upload_to='robots/videos/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.robot_type.name} (VERSION: {self.version})'
    
    class Meta:
        db_table = 'Robot'



class ComponentType(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=200, unique=True)
    descriptive_name = models.CharField(max_length=400, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ComponentType'



class ComponentModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    component_type = models.ForeignKey(ComponentType, on_delete=models.CASCADE, related_name='models')
    model_name = models.CharField(max_length=200, unique=True)
    descriptive_name = models.CharField(max_length=400, null=True, blank=True)
    specifications = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    image = models.ImageField(upload_to='components/images/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.model_name} ({self.component_type.name})'

    class Meta:
        db_table = 'ComponentModel'



class RobotComponent(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    robot_model = models.ForeignKey(Robot, on_delete=models.CASCADE, related_name='components')
    component_model = models.ForeignKey(ComponentModel, on_delete=models.CASCADE, related_name='robot_components')
    quantity = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.robot_model.version} includes {self.quantity} x {self.component_model.model_name}'
                

    class Meta:
        db_table = 'RobotComponent'      
        unique_together = ['robot_model', 'component_model']