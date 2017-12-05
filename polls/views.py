# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return HttpResponse("Hello, this is Polls index page")


def detail(request, question_id):
    return HttpResponse("This view contains the details of the question: %s" % question_id)


def results(request, question_id):
    return HttpResponse("These are the results of the question %s" % question_id)


def vote(request, question_id):
    return HttpResponse("Votes on the question: %s" % question_id)

