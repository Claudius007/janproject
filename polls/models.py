# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone
# Create your models here.
STATUS_CHOICES = (
    ('O', 'Optional'),
    ('C', 'Create'),
    ('udt', 'Update'),
    ('ret', 'Search'),
)


class Question(models.Model):
    question_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('Date Published')

    def __str__(self):
        return self.question_text

    def published_date(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=7)

    published_date.admin_order_field = 'pub_date'
    published_date.boolean = True
    published_date.short_description = "Published this week?"


class Answers(models.Model):
    answer_text = models.CharField(max_length=250)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question)

    def __str__(self):
        return self.answer_text
