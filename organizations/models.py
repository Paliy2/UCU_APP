#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.db import models


class Organization(models.Model):
    id = models.AutoField(primary_key=True, db_index=True, unique=True, editable=False)
    organization_name = models.CharField(max_length=100, blank=False, unique=True)
    head = models.CharField(max_length=1000, blank=False)
    secretary = models.CharField(max_length=1000, blank=False)
    financier = models.CharField(max_length=1000, blank=False)
    members = models.CharField(max_length=10000, blank=False)
    media = models.CharField(max_length=1000, blank=False)
    status = models.CharField(max_length=100, blank=False)


    class Meta:
        '''
        to set table name in database
        '''
        db_table = "organizations"
