import os
import django
import json
import requests
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mockly.settings')
django.setup()

from users.models import User

def seed_users():
    """Seed the database with mock user data"""
    
    # Clear existing data
    User.objects.all().delete()
    print("Cleared existing users...")
    
    # Sample mock users
    mock_users = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "gender": "male",
            "phone": "+1-555-0100",
            "avatar": "https://i.pravatar.cc/150?img=1",
            "street": "123 Main St",
            "city": "New York",
            "state": "NY",
            "country": "USA",
            "postal_code": "10001",
            "job_title": "Software Engineer",
            "company": "TechCorp"
        },
        {
            "first_name": "Jane",
            "last_name": "Smith",
            "email": "jane.smith@example.com",
            "gender": "female",
            "phone": "+1-555-0101",
            "avatar": "https://i.pravatar.cc/150?img=2",
            "street": "456 Oak Ave",
            "city": "Los Angeles",
            "state": "CA",
            "country": "USA",
            "postal_code": "90001",
            "job_title": "Product Manager",
            "company": "Startup Inc"
        },
        {
            "first_name": "Robert",
            "last_name": "Johnson",
            "email": "robert.j@example.com",
            "gender": "male",
            "phone": "+1-555-0102",
            "avatar": "https://i.pravatar.cc/150?img=3",
            "street": "789 Pine Rd",
            "city": "Chicago",
            "state": "IL",
            "country": "USA",
            "postal_code": "60601",
            "job_title": "Data Scientist",
            "company": "DataWorks"
        },
        {
            "first_name": "Emily",
            "last_name": "Williams",
            "email": "emily.w@example.com",
            "gender": "female",
            "phone": "+1-555-0103",
            "avatar": "https://i.pravatar.cc/150?img=4",
            "street": "101 Maple St",
            "city": "Houston",
            "state": "TX",
            "country": "USA",
            "postal_code": "77001",
            "job_title": "UX Designer",
            "company": "DesignStudio"
        },
        {
            "first_name": "Michael",
            "last_name": "Brown",
            "email": "michael.b@example.com",
            "gender": "male",
            "phone": "+1-555-0104",
            "avatar": "https://i.pravatar.cc/150?img=5",
            "street": "202 Cedar Ln",
            "city": "Phoenix",
            "state": "AZ",
            "country": "USA",
            "postal_code": "85001",
            "job_title": "DevOps Engineer",
            "company": "CloudSystems"
        },
        {
            "first_name": "Sarah",
            "last_name": "Davis",
            "email": "sarah.d@example.com",
            "gender": "female",
            "phone": "+1-555-0105",
            "avatar": "https://i.pravatar.cc/150?img=6",
            "street": "303 Birch Blvd",
            "city": "Philadelphia",
            "state": "PA",
            "country": "USA",
            "postal_code": "19101",
            "job_title": "Marketing Director",
            "company": "GrowthCo"
        },
        {
            "first_name": "David",
            "last_name": "Miller",
            "email": "david.m@example.com",
            "gender": "male",
            "phone": "+1-555-0106",
            "avatar": "https://i.pravatar.cc/150?img=7",
            "street": "404 Elm St",
            "city": "San Antonio",
            "state": "TX",
            "country": "USA",
            "postal_code": "78201",
            "job_title": "Sales Executive",
            "company": "SalesPro"
        },
        {
            "first_name": "Lisa",
            "last_name": "Wilson",
            "email": "lisa.w@example.com",
            "gender": "female",
            "phone": "+1-555-0107",
            "avatar": "https://i.pravatar.cc/150?img=8",
            "street": "505 Walnut Ave",
            "city": "San Diego",
            "state": "CA",
            "country": "USA",
            "postal_code": "92101",
            "job_title": "HR Manager",
            "company": "PeopleFirst"
        },
        {
            "first_name": "James",
            "last_name": "Moore",
            "email": "james.m@example.com",
            "gender": "male",
            "phone": "+1-555-0108",
            "avatar": "https://i.pravatar.cc/150?img=9",
            "street": "606 Spruce Dr",
            "city": "Dallas",
            "state": "TX",
            "country": "USA",
            "postal_code": "75201",
            "job_title": "CTO",
            "company": "InnovateTech"
        },
        {
            "first_name": "Amanda",
            "last_name": "Taylor",
            "email": "amanda.t@example.com",
            "gender": "female",
            "phone": "+1-555-0109",
            "avatar": "https://i.pravatar.cc/150?img=10",
            "street": "707 Ash Ct",
            "city": "San Jose",
            "state": "CA",
            "country": "USA",
            "postal_code": "95101",
            "job_title": "CEO",
            "company": "Visionary Inc"
        }
    ]
    
    # Create users
    users_created = 0
    for user_data in mock_users:
        user, created = User.objects.get_or_create(
            email=user_data['email'],
            defaults=user_data
        )
        if created:
            users_created += 1
    
    print(f"✅ Seeded {users_created} mock users")
    return users_created

if __name__ == "__main__":
    seed_users()