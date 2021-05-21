#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import uuid
from django.db import models
from user.models import User



class Event(models.Model):
    # todo get the list of categories for events
    STATUS_CHOICES = [
        ('d', 'Draft'),
        ('r', 'To be reviewd'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    ]

    categories = ((1, "Sociology"),
                  (2, "Programming"),
                  (3, "Lifeworks"),
                  )

    location_choices = (('c', "Sheptytsky Center"),
                        ('k', "Kozelnytska 2a"),
                        ('s', "Sventsitskoho 17"),
                        ('h', "Khutorivka"),
                        )

    id = models.AutoField(primary_key=True)
    # id = models.AutoField(null=True)
    status = models.CharField(max_length=1, default='d', choices=STATUS_CHOICES)

    picture_url = models.URLField()
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    # todo user model created by FK
    created_by = models.CharField(max_length=200, blank=False)
    lecturer = models.CharField(max_length=200)

    category = models.IntegerField(choices=categories)
    location = models.CharField(max_length=300, choices=location_choices)
    event_datetime = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_online = models.BooleanField(default=False)
    event_online_meeting_link = models.CharField(max_length=600, blank=True)

    class Meta:
        '''
        to set table name in database
        '''
        db_table = "events"


class EventFavorites(models.Model):
    event_id = models.ForeignKey(Event, verbose_name="Event id", on_delete=models.CASCADE)
    user = models.EmailField(max_length=200)

    class Meta:
        db_table = "event_favorites"
