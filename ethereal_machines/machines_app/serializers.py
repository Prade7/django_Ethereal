# machines_app/serializers.py
from rest_framework import serializers
from .models import Machine, DynamicData
# class MachineSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Machine
#         fields = ['id', 'name', 'acceleration', 'velocity']




# machines_app/serializers.py
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Include custom claims
        token['employee_id'] = user.employee_id
        token['role'] = user.role

        return token


class DynamicDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DynamicData
        fields = [
            'actual_position_x', 'actual_position_y', 'actual_position_z',
            'actual_position_a', 'actual_position_c',
            'distance_to_go_x', 'distance_to_go_y', 'distance_to_go_z',
            'distance_to_go_a', 'distance_to_go_c',
            'homed_x', 'homed_y', 'homed_z', 'homed_a', 'homed_c',
            'tool_offset_x', 'tool_offset_y', 'tool_offset_z',
            'tool_offset_a', 'tool_offset_c',
            'created_by', 'timestamp'
        ]

class MachineSerializer(serializers.ModelSerializer):
    dynamic_data = DynamicDataSerializer(many=True, read_only=True)

    class Meta:
        model = Machine
        fields = ['name', 'acceleration', 'velocity', 'dynamic_data']