from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    JobApplicationViewSet,
    CompanyViewSet,
    register_user,
    subscription_view,
    user_profile_view,
    generate_interview_questions,
    CustomTokenObtainPairView,
    test_password,
    test_view  # Make sure this is imported
)

router = DefaultRouter()
router.register(r'job-applications', JobApplicationViewSet, basename='job-application')
router.register(r'companies', CompanyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user, name='register'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('subscription/', subscription_view, name='subscription'),
    path('profile/', user_profile_view, name='user_profile'),
    path('interview-questions/', generate_interview_questions, name='interview_questions'),
    path('test-password/', test_password, name='test_password'),
    path('test/', test_view, name='test_view'),  # Make sure this line is present
]