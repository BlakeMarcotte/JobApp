from rest_framework import serializers
from .models import JobApplication, Company, Subscription, UserProfile
from django.contrib.auth.models import User

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'website', 'description']

class JobApplicationSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    company_id = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(), source='company', write_only=True
    )

    class Meta:
        model = JobApplication
        fields = ['id', 'company', 'company_id', 'position', 'description', 'application_date', 'status', 'salary', 'notes']
        read_only_fields = ['id']

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['tier', 'active']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['phone', 'resume', 'cover_letter', 'about']