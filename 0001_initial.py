# Generated by Django 5.2.3 on 2025-06-22 14:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Applicant_Name', models.CharField(max_length=100)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('District', models.CharField(max_length=100)),
                ('State', models.CharField(max_length=100)),
                ('Pincode', models.IntegerField()),
                ('Ownership', models.CharField(choices=[('Individual', 'Individual'), ('Joint', 'Joint')], max_length=20)),
                ('GovtID_Type', models.CharField(choices=[('Aadhar', 'Aadhar'), ('Voter_Id', 'Voter_Id'), ('PAN', 'PAN'), ('Passport', 'Passport')], max_length=20)),
                ('ID_Number', models.CharField(max_length=100)),
                ('Category', models.CharField(choices=[('Residential', 'Residential'), ('Commercial', 'Commercial')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status_Name', models.CharField(choices=[('Connection Released', 'Connection Released'), ('Approved', 'Approved'), ('Pending', 'Pending'), ('Rejected', 'Rejected')], max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Load_Applied', models.IntegerField()),
                ('Date_of_Application', models.DateField()),
                ('Date_of_Approval', models.DateField(blank=True, null=True)),
                ('Modified_Date', models.DateField(blank=True, null=True)),
                ('Reviewer_ID', models.IntegerField()),
                ('Reviewer_Name', models.CharField(max_length=100)),
                ('Reviewer_Comments', models.CharField(choices=[('Installation pending', 'Installation pending'), ('Documents verification in progress', 'Documents verification in progress'), ('Installation completed', 'Installation completed'), ('KYC failed', 'KYC failed')], max_length=50)),
                ('Applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.applicant')),
                ('Status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.status')),
            ],
        ),
    ]
