# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.contrib import admin
from .models import Question, Answers
from django.utils import timezone

# Register your models here


# def make_published(modeladmin, request, queryset):
# queryset.update(status='p')
# quest_new = Question.published_date
# quest_new.boolean = True
# make_published.short_description = "Mark selected stories as published"


class AnswersInline(admin.StackedInline):
    extra = 3
    model = Answers


# @admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):

    fieldsets = [(None, {'fields': ['question_text']}), ('Date_Information', {'fields': ['pub_date']})]
    inlines = [AnswersInline]

    list_display = ('question_text', 'pub_date', 'published_date')

    actions = [Question.published_date]

    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answers)
