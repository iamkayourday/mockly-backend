from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()
    full_address = serializers.ReadOnlyField()
    
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'full_name',
            'email',
            'gender',
            'phone',
            'avatar',
            'street',
            'city',
            'state',
            'country',
            'postal_code',
            'full_address',
            'job_title',
            'company',
            'created_at',
        ]