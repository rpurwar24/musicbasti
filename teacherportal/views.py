# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render_to_response, render,redirect
from django.template import RequestContext, loader
from django.http import *
from core.models import *
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth
from django.contrib.auth import logout as auth_logout

def index(request):
    return render(request, 'index.html',
    	{
    	}
    )


def attendance(request):
    return render(request, 'attendance.html',
    	{
    	}
    )

def logout(request):
    auth_logout(request)
    return redirect('/teacher-portal')