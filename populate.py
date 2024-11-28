#Ampiasaina amle shell ito fa tsy executena direct

from faker import Faker
from sehatra.models import User


fake = Faker()

def generate_fake_data():
    for _ in range(50):
        username = fake.user_name()
        email = f"{fake.user_name()}@gmail.com"
        password = fake.password(length=12) 
        created_at = fake.date_time_between(start_date='-2y', end_date='now')

        # unique values for email and username
        while User.objects.filter(username=username).exists():
            username = fake.user_name()

        while User.objects.filter(email=email).exists():
            email = fake.email()

        User.objects.create(
            username=username,
            email=email,
            password=password,
            created_at=created_at,
        )
