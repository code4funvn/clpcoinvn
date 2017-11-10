# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def home(request):
    context_dict = {}
    return render(request, 'clpcoin/home.html', context_dict)