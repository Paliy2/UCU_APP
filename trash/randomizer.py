import sys, os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UCU_APP.settings')

import django

django.setup()

import random
import names
import string
from user.serializers import UserRegistrationSerializer
from organizations.serializers import OrganizationSerializer, DepartmentSerializer
from organizations.models import Organization, Department
from profile.serializers import PhoneNumberSerializer
import pandas as pd


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
        return random.randint(10 ** 10, 10 ** 11)

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


def create_student_organizations(path="../staticfiles/SO_UCU2.csv"):
    df = pd.read_csv(path, encoding="windows-1251", sep=';')
    for index, row in df.iterrows():
        res = {
            "organization_name": df["Organization"][index],
            "head": df["Head"][index],
            "secretary": df["Secretary"][index],
            "financier": df["Financier"][index],
            "members": df["MembersNames"][index],
            "media": df["MediaLinks"][index],
            "status": df["Status"][index],
        }
        # todo save res in DB
        try:
            OrganizationSerializer().create(validated_data=res)
        except:
            print(res)


def create_contacts(path="../staticfiles/contacts.csv"):
    df = pd.read_csv(path, encoding="utf-8", sep=',')
    for index, row in df.iterrows():
        res = {
            "emailucu": df["emailucu"][index],
            "lastnameukr": df["lastnameukr"][index],
            "firstnameukr": df["firstnameukr"][index],
            "lastnameeng": df["lastnameeng"][index],
            "firstnameeng": df["firstnameeng"][index],
            "phone": df["phone"][index],
            "department": df["department"][index],
        }
        # print(res)
        # todo save res in DB
        try:
            PhoneNumberSerializer().create(validated_data=res)
        except:
            print(res)


def create_departments(path="../staticfiles/departments.csv"):
    df = pd.read_csv(path, encoding="windows-1251", sep=';')
    for index, row in df.iterrows():
        res = {
             "department_name": df["DepartmentName"][index],
            "web_site": df["webSite"][index],
        }
        # print(res)
        # todo save res in DB
        try:
            DepartmentSerializer().create(validated_data=res)
        except:
            print(res)


if __name__ == '__main__':
    # USERS_TO_CREATE = 100
    #
    # user_manager = UserRegistrationSerializer()
    # generator = RandomUserAccountGenerator()
    # for i in range(USERS_TO_CREATE):
    #     data = generator.get_new_json()
    #     user_manager.create(data)
    # print("Finished")
    # create_contacts()
    # create_student_organizations()
    create_departments()
