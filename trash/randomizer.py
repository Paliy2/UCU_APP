import sys, os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UCU_APP.settings')

import django
django.setup()

import random
import names
import string
from user.serializers import UserRegistrationSerializer


class RandomUserAccountGenerator:
    def __init__(self):
        pass

    def get_sex(self):
        return 'male' if random.randint(0, 1) == 0 else 'female'

    @staticmethod
    def get_random_name(gender='male'):
        return names.get_first_name(gender)

    @staticmethod
    def get_random_surname(gender='male'):
        return names.get_last_name()

    @staticmethod
    def get_random_age():
        return random.randint(18, 100)

    @staticmethod
    def get_random_phone():
        return random.randint(10**10, 10**11)

    @staticmethod
    def get_random_char(y):
        return ''.join(random.choice(string.ascii_letters) for x in range(y))

    def get_random_mail(self):
        return self.get_random_char(random.randint(5, 14)) + "@gmail.com"

    def get_new_json(self):
        gender = self.get_sex()
        profile = {
            'first_name': self.get_random_name(gender),
            'last_name': self.get_random_surname(gender),
            'gender': gender,
            'age': self.get_random_age(),
            'phone_number': self.get_random_phone(),
        }
        return {
            'email': self.get_random_mail(),
            'password': self.get_random_name(),
            'profile': profile,
        }

if __name__ == '__main__':
    USERS_TO_CREATE = 100

    user_manager = UserRegistrationSerializer()
    generator = RandomUserAccountGenerator()
    for i in range(USERS_TO_CREATE):
        data = generator.get_new_json()
        user_manager.create(data)
    print("Finished")

