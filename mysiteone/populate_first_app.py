import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysiteone.settings")

import django
django.setup()

from first_app.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for item in range(N):
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()

        all_users = User.objects.get_or_create(first_name=fake_first_name, last_name = fake_last_name, email = fake_email)[0]

if __name__ == "__main__":
    populate(20)

    