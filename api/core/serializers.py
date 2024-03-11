from rest_framework import serializers
from .models import Vessel, VesselSchedule, BillOfLading, Container

class VesselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vessel
        fields = ['vessel_name', 'id']
        read_only_fields = ['id']

class VesselScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VesselSchedule
        fields = ['vessel', 'voyage_number', 'arrival_date', 'id']
        read_only_fields = ['id']

class BillOfLadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillOfLading
        fields = ['voyage', 'bol_number', 'contact_name', 'contact_number', 'contact_email', 'release_status', 'id']
        read_only_fields = ['id']

class ContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Container
        fields = ['container_number', 'bol', 'id']
        read_only_fields = ['id']