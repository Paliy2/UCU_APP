#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import uuid
from datetime import datetime, timedelta

from django.core.validators import validate_comma_separated_integer_list
from django.db import models
from user.models import User
from django import forms


def default_start_time():
    now = datetime.now()
    return now + timedelta(hours=1)

class Choice(models.Model):
    categories = ((1, "Sociology"),
                  (2, "Programming"),
                  (3, "Lifeworks"),
                  )
    choice = models.CharField(choices=categories, max_length=150, unique=True)


class Event(models.Model):
    # todo get the list of categories for events
    STATUS_CHOICES = [
        ('d', 'Draft'),
        ('r', 'To be reviewd'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    ]

    location_choices = (('c', "Sheptytsky Center"),
                        ('k', "Kozelnytska 2a"),
                        ('s', "Sventsitskoho 17"),
                        ('h', "Khutorivka"),
                        )

    # id = models.AutoField(primary_key=True, unique=True, default=1000)
    id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
    # id = models.AutoField(null=True)
    status = models.CharField(max_length=1, default='d', choices=STATUS_CHOICES)

    image = models.ImageField(blank=True, upload_to="media/")
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    # todo user model created by FK
    created_by = models.CharField(max_length=200, blank=False)
    lecturer = models.CharField(max_length=200)

    # category = models.IntegerField(choices=categories)
    # category = models.CharField(validators=[validate_comma_separated_integer_list], max_length=255, default='1', blank=True)
    category = models.CharField(max_length=2505, default='1', blank=True)
    # location = models.CharField(max_length=300, choices=location_choices)
    location = models.CharField(max_length=3000, blank=True)
    event_datetime = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_online = models.BooleanField(default=False)
    event_online_meeting_link = models.CharField(max_length=600, blank=True)

    class Meta:
        ordering = ("event_datetime", )
        db_table = "events"


class EventFavorites(models.Model):
    event_id = models.ForeignKey(Event, verbose_name="Event id", on_delete=models.CASCADE)
    user = models.EmailField(max_length=200)

    class Meta:
        db_table = "event_favorites"
