from django.http import HttpResponse
from django.shortcuts import render
from .models import Bb


def index(request):
    s = 'List of Ads\n\n\n'
    for bb in Bb.objects.order_by('-published'):
        s += bb.title + '\n' + bb.content + '\n\n'
    return HttpResponse(s, content_type='text/plain; charset=utf-8')
