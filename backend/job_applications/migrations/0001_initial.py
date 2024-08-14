# Generated by Django 5.1 on 2024-08-14 02:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('website', models.URLField(blank=True, null=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='job_applications.company')),
            ],
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('application_date', models.DateField()),
                ('status', models.CharField(choices=[('APPLIED', 'Applied'), ('IN_PROGRESS', 'In Progress'), ('REJECTED', 'Rejected'), ('OFFER', 'Offer Received'), ('ACCEPTED', 'Offer Accepted')], default='APPLIED', max_length=20)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('notes', models.TextField(blank=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_applications', to='job_applications.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_applications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('interview_type', models.CharField(choices=[('PHONE', 'Phone'), ('VIDEO', 'Video'), ('IN_PERSON', 'In-Person'), ('TECHNICAL', 'Technical')], max_length=20)),
                ('notes', models.TextField(blank=True)),
                ('interviewer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='job_applications.contact')),
                ('job_application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interviews', to='job_applications.jobapplication')),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='job_application',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='job_applications.jobapplication'),
        ),
    ]
