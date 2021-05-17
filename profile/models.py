#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import uuid
from django.db import models
from user.models import User


class PhoneNumber(models.Model):

    # id = models.AutoField(primary_key=True, db_index=True, unique=True, editable=False)
    emailucu = models.EmailField()
    lastnameukr = models.CharField(max_length=1000, unique=False)
    firstnameukr = models.CharField(max_length=1000, unique=False)
    lastnameeng = models.CharField(max_length=1000, unique=False)
    firstnameeng = models.CharField(max_length=1000, unique=False)
    phone = models.CharField(max_length=1000, unique=False)
    department = models.CharField(max_length=1000, unique=False)

    class Meta:
        db_table = "contacts"

class UserProfile(models.Model):

    id = models.AutoField(primary_key=True, db_index=True, unique=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50, unique=False)
    last_name = models.CharField(max_length=50, unique=False)
    phone_number = models.CharField(max_length=13, unique=True, null=False, blank=False)
    age = models.PositiveIntegerField(null=False, blank=False)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    class Meta:
        '''
        to set table name in database
        '''
        db_table = "profile"