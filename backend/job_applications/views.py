from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import JobApplication, Company, Subscription, UserProfile
from .serializers import JobApplicationSerializer, CompanySerializer, UserSerializer, SubscriptionSerializer, UserProfileSerializer
from django.contrib.auth.models import User
import logging
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from django.db import connection
from django.http import JsonResponse
import json
from django.http import JsonResponse

def test_view(request):
    return JsonResponse({"message": "Test view is working"})


logger = logging.getLogger(__name__)

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        logger.info(f"Login attempt for user: {username}")
        
        user = authenticate(username=username, password=password)
        if user is None:
            logger.warning(f"Authentication failed for user: {username}")
            if User.objects.filter(username=username).exists():
                logger.warning(f"User exists but password is incorrect: {username}")
            else:
                logger.warning(f"User does not exist: {username}")
        else:
            logger.info(f"Authentication successful for user: {username}")
        
        response = super().post(request, *args, **kwargs)
        
        if response.status_code == 200:
            logger.info(f"Token generated successfully for user: {username}")
        else:
            logger.warning(f"Token generation failed for user: {username}")
        
        return response

class JobApplicationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = JobApplicationSerializer

    def get_queryset(self):
        return JobApplication.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CompanyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    logger.info(f"Received registration request: {request.data}")
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        if user:
            logger.info(f"User created successfully: {user.username}")
            logger.info(f"Password hash: {user.password[:20]}...")  # Log first 20 chars of password hash
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    logger.error(f"User creation failed. Errors: {serializer.errors}")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def subscription_view(request):
    if request.method == 'GET':
        subscription, created = Subscription.objects.get_or_create(user=request.user)
        serializer = SubscriptionSerializer(subscription)
        return Response(serializer.data)
    elif request.method == 'POST':
        subscription, created = Subscription.objects.get_or_create(user=request.user)
        serializer = SubscriptionSerializer(subscription, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def user_profile_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'GET':
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = UserProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def generate_interview_questions(request):
    company = request.data.get('company', '')
    position = request.data.get('position', '')
    field = request.data.get('field', '')

    questions = [
        f"Why do you want to work at {company}?",
        f"What experience do you have that's relevant to the {position} role?",
        f"Can you describe a challenging situation you've faced in your {field} work?",
        "Where do you see yourself in 5 years?",
        "What are your strengths and weaknesses?",
    ]

    return Response({'questions': questions})

@csrf_exempt
def test_password(request):
    if request.method == 'POST':
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
        else:
            username = request.POST.get('username')
            password = request.POST.get('password')

        if not username or not password:
            return JsonResponse({'message': 'Username and password are required'}, status=400)

        # Print database connection info
        print(f"Database connection: {connection.settings_dict['NAME']}")

        # Query the database and print the result
        user_query = User.objects.filter(username=username)
        print(f"User query: {user_query.query}")
        user = user_query.first()

        if user:
            if check_password(password, user.password):
                return JsonResponse({'message': 'Password is correct'})
            else:
                return JsonResponse({'message': 'Password is incorrect'})
        else:
            # Print all usernames in the database
            all_users = User.objects.all()
            print(f"All users in database: {[u.username for u in all_users]}")
            return JsonResponse({'message': 'User not found', 'all_users': [u.username for u in all_users]}, status=404)
    return JsonResponse({'message': 'Please use POST method'}, status=405)