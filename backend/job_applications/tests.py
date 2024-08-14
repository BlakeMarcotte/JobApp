from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import JobApplication, Company


class JobApplicationTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.company = Company.objects.create(name='Test Company')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_job_application(self):
        data = {
            'company_id': self.company.id,
            'position': 'Software Engineer',
            'description': 'A great job opportunity',
            'application_date': '2023-08-14',
            'status': 'APPLIED'
        }
        response = self.client.post('/api/job-applications/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(JobApplication.objects.count(), 1)
        self.assertEqual(JobApplication.objects.get().position, 'Software Engineer')

    def test_list_job_applications(self):
        JobApplication.objects.create(
            user=self.user,
            company=self.company,
            position='Data Scientist',
            application_date='2023-08-14',
            status='APPLIED'
        )
        response = self.client.get('/api/job-applications/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['position'], 'Data Scientist')

    def test_update_job_application(self):
        job_app = JobApplication.objects.create(
            user=self.user,
            company=self.company,
            position='Frontend Developer',
            application_date='2023-08-14',
            status='APPLIED'
        )
        data = {'status': 'IN_PROGRESS'}
        response = self.client.patch(f'/api/job-applications/{job_app.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(JobApplication.objects.get(id=job_app.id).status, 'IN_PROGRESS')

    def test_delete_job_application(self):
        job_app = JobApplication.objects.create(
            user=self.user,
            company=self.company,
            position='Product Manager',
            application_date='2023-08-14',
            status='APPLIED'
        )
        response = self.client.delete(f'/api/job-applications/{job_app.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(JobApplication.objects.count(), 0)